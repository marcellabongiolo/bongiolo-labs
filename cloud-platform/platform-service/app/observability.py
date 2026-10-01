import logging
import time
import uuid

from fastapi import Request


logger = logging.getLogger("bongiolo.platform")


async def request_observability(request: Request, call_next):
    request_id = str(uuid.uuid4())
    started = time.perf_counter()

    response = await call_next(request)

    duration_ms = round((time.perf_counter() - started) * 1000, 2)
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
