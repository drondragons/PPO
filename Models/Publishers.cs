#nullable disable

namespace BLComponent
{
    public class Publisher
    {
        private ushort _id;
        private string _title;
        private byte _country_id;

        public ushort ID
        {
            get { return _id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "ID");
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

        public byte CountryID
        {
            get { return _country_id; }
            set 
            {
                FieldValidator.Validate(value, 1, byte.MaxValue, "country ID");
                _country_id = value;
            }
        }

        public Publisher(ushort id, string title, byte country_id)
        {
            ID = id;
            Title = title;
            CountryID = country_id;
        }
    }
}