from main import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    receipt_number = db.Column(db.String(10), nullable=False, unique=True)
    transaction_date = db.Column(db.BigInteger, nullable=False)

    def __repr__(self) -> str:
        data = {
            'id': self.id,
            'amount': self.amount,
            'phone': self.phone_number,
            'receipt': self.receipt_number,
            'date': self.transaction_date
        }
        return f'Transaction({str(data)})'
