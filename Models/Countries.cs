#nullable disable

namespace BLComponent
{
    public class Country
    {
        private byte _id;
        private string _title;

        public byte ID
        {
            get { return _id; }
            set 
            {
                FieldValidator.Validate(value, 1, byte.MaxValue, "ID");
                _id = value;
            }
        }

        public string Title
        {
            get { return _title; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, field_name: "название");
                _title = value;
            }
        }

        public Country(byte id, string title)
        {
            ID = id;
            Title = title;
        }
    }
}