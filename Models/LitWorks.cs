#nullable disable

namespace BLComponent
{
    public class LitWork
    {
        private ushort _id;
        private string _title;
        private ushort? _writing_year;
        private string _description;
        private string _text_path;

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

        public ushort? WritingYear
        {
            get { return _writing_year; }
            set 
            {
                if (value != null) FieldValidator.Validate((ushort)value, (ushort)1500, (ushort)DateTime.Now.Year, "год написания");
                _writing_year = value;
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

        public string TextPath
        {
            get { return _text_path; }
            set 
            {
                FieldValidator.Validate(value, pattern: "^\\.\\./TableData/BooksEpub/[0-9а-яА-ЯёЁa-zA-Z_-]+\\.epub$", field_name: "текст");
                _text_path = value;
            }
        }

        public LitWork(ushort id, string title, ushort? writing_year, string description, string text_path)
        {
            ID = id;
            Title = title;
            WritingYear = writing_year;
            Description = description;
            TextPath = text_path;
        }
    }
}