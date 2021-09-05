from typer import echo


def create_all() -> None:
    from admin_original.db import metadata
    from admin_original.db.utils.settings import DBSettings

    db_settings = DBSettings()

    db_settings.setup_db()
    echo('creating')
    metadata.create_all()
    echo('complete!')


if __name__ == "__main__":
    create_all()
