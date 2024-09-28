from datetime import datetime


class Contract:
    def __init__(self, id: int, created_date: datetime, updated_date: datetime,
                 obligor_client_id: int, obligatee_client_id: int, text: str, face_value: int):
        self.id = id
        self.created_date = created_date
        self.updated_date = updated_date
        self.obligor_client_id = obligor_client_id
        self.obligatee_client_id = obligatee_client_id
        self.text = text
        self.face_value = face_value

    def __repr__(self) -> str:
        return (f"Contract(id={self.id}, created_date={self.created_date}, updated_date={self.updated_date}, "
                f"obligor_client_id={self.obligor_client_id}, obligatee_client_id={
                    self.obligatee_client_id}, "
                f"text='{self.text}', face_value={self.face_value})")
