from sqlalchemy.orm import Session
from app.db.session import engine
from app.models.rank import Base as rank_model
from app.models.affiliation import Base as affiliation_model
from app.models.military_unit import Base as military_unit_model
from app.models.role import Base as role_model
from app.models.user import Base as user_model
from app.models.uniform import Base as uniform_model
from app.models.access_log import Base as access_log_model
from app.models.inspection_log import Base as inspection_log_model
from app.models.appearance import Base as appearance_model
from app.models.inspection_detail import Base as inspection_detail_model
from app.crud import rank as rank_crud
from app.crud import affiliation as affiliation_crud
from app.crud import role as role_crud
from app.crud import uniform as uniform_crud
from app.crud import appearance as appearance_crud


def init_db(db: Session):
    rank_model.metadata.create_all(bind=engine)
    rank_crud.create_rank(db, 1, "이병")
    rank_crud.create_rank(db, 2, "일병")
    rank_crud.create_rank(db, 3, "상병")
    rank_crud.create_rank(db, 4, "병장")

    affiliation_model.metadata.create_all(bind=engine)
    affiliation_crud.create_affiliation(db, 1, "육군")
    affiliation_crud.create_affiliation(db, 2, "해군")
    affiliation_crud.create_affiliation(db, 3, "공군")
    affiliation_crud.create_affiliation(db, 4, "해병대")

    role_model.metadata.create_all(bind=engine)
    role_crud.create_role(db, 1, "user")
    role_crud.create_role(db, 2, "admin")
    role_crud.create_role(db, 3, "super")

    user_model.metadata.create_all(bind=engine)

    military_unit_model.metadata.create_all(bind=engine)

    uniform_model.metadata.create_all(bind=engine)
    uniform_crud.create_uniform(db, 1, "샘당")
    uniform_crud.create_uniform(db, 2, "정복")
    uniform_crud.create_uniform(db, 3, "군복")

    access_log_model.metadata.create_all(bind=engine)
    inspection_log_model.metadata.create_all(bind=engine)

    appearance_model.metadata.create_all(bind=engine)
    appearance_crud.create_appearance(db, 1, "두발")
    appearance_crud.create_appearance(db, 2, "이름표")
    appearance_crud.create_appearance(db, 3, "계급장")
    appearance_crud.create_appearance(db, 4, "태극기")
    appearance_crud.create_appearance(db, 5, "모자")
    appearance_crud.create_appearance(db, 6, "네커치프")
    appearance_crud.create_appearance(db, 7, "머플러")

    inspection_detail_model.metadata.create_all(bind=engine)
