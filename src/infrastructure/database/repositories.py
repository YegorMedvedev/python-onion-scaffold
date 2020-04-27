from typing import Optional

from sqlalchemy.orm import Session

import app
import core.domain_entity_interfaces as interface
import infrastructure.database.models as model


class ApplicationRepository:
    session: Session
    schema: str = "public"

    def __init__(self):
        self.session = app.database.session()

    def select_latest_migration(self) -> Optional[interface.AlembicVersion]:
        result = self.session.query(model.AlembicVersion).first()
        if result is None:
            return None
        else:
            return interface.AlembicVersion(version=result.__dict__["version_num"])
