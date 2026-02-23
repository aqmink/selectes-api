from typing import Awaitable, Callable

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.core.config import settings


def create_scheduler(job: Callable[[], Awaitable[None]]) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        job,
        trigger="interval",
        minutes=settings.parse_schedule_minutes, # Расхожление во времени: вакансии прибывают каждые 5 секунд, не минут?
        coalesce=True,
        max_instances=1,
        misfire_grace_time=30, # Фикс пропуска джоб из-за опоздания
    )
    return scheduler
