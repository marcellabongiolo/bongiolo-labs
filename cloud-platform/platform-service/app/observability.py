import logging
import time
import uuid

from fastapi import Request
from prometheus_client import Counter, Histogram

logger = logging.getLogger("bongiolo.platform")

REQUEST_COUNT = Counter(
    "platform_http_requests_total",
    "Total number of HTTP requests.",
    ["method", "path", "status"],
)

REQUEST_ERRORS = Counter(
    "platform_http_errors_total",
    "Total number of HTTP 5xx responses.",
    ["method", "path"],
)

REQUEST_LATENCY = Histogram(
    "platform_http_request_duration_seconds",
    "HTTP request duration in seconds.",
    ["method", "path"],
)


async def request_observability(request: Request, call_next):
    request_id = str(uuid.uuid4())
    started = time.perf_counter()

    try:
        response = await call_next(request)
    except Exception:
        duration_seconds = time.perf_counter() - started
        REQUEST_ERRORS.labels(request.method, request.url.path).inc()
        REQUEST_LATENCY.labels(request.method, request.url.path).observe(duration_seconds)
        logger.exception(
            "request_failed",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": 500,
                "duration_ms": round(duration_seconds * 1000, 2),
            },
        )
        raise

    duration_seconds = time.perf_counter() - started
    duration_ms = round(duration_seconds * 1000, 2)

    REQUEST_COUNT.labels(
        request.method, request.url.path, str(response.status_code)
    ).inc()
    REQUEST_LATENCY.labels(request.method, request.url.path).observe(duration_seconds)

    if response.status_code >= 500:
        REQUEST_ERRORS.labels(request.method, request.url.path).inc()

    response.headers["X-Request-ID"] = request_id

    logger.info(
        "request_completed",
        extra={
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": duration_ms,
        },
    )

    return response
