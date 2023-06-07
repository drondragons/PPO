#nullable disable

namespace BLComponent
{
    public class Author
    {
        private ushort _id;
        private string _initials;
        private DateOnly? _birth_date;
        private DateOnly? _death_date;
        private string _photo_path;
        private string _biography;

        public ushort ID
        {
            get { return _id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "ID");
                _id = value;
            }
        }

        public string Initials
        {
            get { return _initials; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, pattern: "^[А-ЯЁ][а-яА-ЯёЁ-]* [А-ЯЁ][а-яА-ЯёЁ-]*$", field_name: "инициалы");
                _initials = value;
            }
        }

        public DateOnly? BirthDate
        {
            get { return _birth_date; }
            set 
            {
                FieldValidator.Validate(value, new DateOnly(1500, 1, 1), DateOnly.FromDateTime(DateTime.Now), true, "дата рождения");
                _birth_date = value;
            }
        }

        public DateOnly? DeathDate
        {
            get { return _death_date; }
            set 
            {
                FieldValidator.Validate(value, new DateOnly(1500, 1, 1), DateOnly.FromDateTime(DateTime.Now), true, "дата смерти");
                _death_date = value;
            }
        }

        public string PhotoPath
        {
            get { return _photo_path; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, pattern: "^\\.\\./TableData/AuthorsPhoto/[0-9а-яА-ЯёЁa-zA-Z_-]+\\.(png|jpg|jpeg)$", field_name: "фото");
                _photo_path = value;
            }
        }

        public string Biography
        {
            get { return _biography; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, field_name: "биография");
                _biography = value;
            }
        }

        public Author(ushort id, string initials, DateOnly? birth_date, DateOnly? death_date, string photo_path = "../TableData/AuthorsPhoto/default_author_photo.jpg", string biography = default)
        {
            ID = id;
            Initials = initials;
            BirthDate = birth_date;
            DeathDate = death_date;
            if (BirthDate != null && DeathDate != null && ((DateOnly)DeathDate) < ((DateOnly)BirthDate))
                throw new ArgumentException($"Дата смерти должна быть позже даты рождения!");
            if (BirthDate != null && DeathDate != null && (((DateOnly)DeathDate).Year - ((DateOnly)BirthDate).Year) > 150)
                throw new ArgumentException($"Возраст человека не может быть больше 150 лет!");
            PhotoPath = photo_path;
            Biography = biography;
        }
    }
}