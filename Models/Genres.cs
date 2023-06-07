#nullable disable

namespace BLComponent
{
    public class Genre
    {
        private ushort _id;
        private string _title;
        private string _description;

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

        public string Description
        {
            get { return _description; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, field_name: "описание");
                _description = value;
            }
        }

        public Genre(ushort id, string title, string description)
        {
            ID = id;
            Title = title;
            Description = description;
        }
    }
}