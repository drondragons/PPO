#nullable disable

namespace BLComponent
{
    public class BookRegistration
    {
        private uint _id;
        private ushort _user_id;
        private ushort _book_id;
        private byte _book_status_id;
        private ushort _book_amount;
        private DateTime? _registration_date;

        public uint ID
        {
            get { return _id; }
            set 
            {
                FieldValidator.Validate(value, 1, uint.MaxValue, "ID");
                _id = value;
            }
        }

        public ushort UserID
        {
            get { return _user_id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "user ID");
                _user_id = value;
            }
        }

        public ushort BookID
        {
            get { return _book_id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "book ID");
                _book_id = value;
            }
        }

        public byte BookStatusID
        {
            get { return _book_status_id; }
            set 
            {
                FieldValidator.Validate(value, 1, byte.MaxValue, "book status ID");
                _book_status_id = value;
            }
        }

        public ushort BookAmount
        {
            get { return _book_amount; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "количество книг");
                _book_amount = value;
            }
        }

        public DateTime? RegistrationDate
        {
            get { return _registration_date; }
            set 
            {
                FieldValidator.Validate(value, false, "дата, время регистрации книг");
                _registration_date = value;
            }
        }

        public BookRegistration(uint id, ushort user_id, ushort book_id, byte book_status_id, ushort book_amount, DateTime? registration_date)
        {
            ID = id;
            UserID = user_id;
            BookID = book_id;
            BookStatusID = book_status_id;
            BookAmount = book_amount;
            RegistrationDate = registration_date;
        }
    }
}