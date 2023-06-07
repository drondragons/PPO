#nullable disable

namespace BLComponent
{
    public class BookStatus
    {
        private byte _id;
        private string _book_status;

        public byte ID 
        {
            get { return _id; }
            set 
            {
                FieldValidator.Validate(value, 1, byte.MaxValue, "ID");
                _id = value;
            }
        }

        public string Name 
        {
            get { return _book_status; }
            set
            {
                FieldValidator.Validate(value, _nullable: false, field_name: "книжный статус");
                _book_status = value;
            }
        }

        public BookStatus(byte id, string name)
        {
            ID = id;
            Name = name;
        }
    }
}