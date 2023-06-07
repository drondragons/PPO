#nullable disable

namespace BLComponent
{
    public class User 
    {
        private ushort _id;
        private string _login;
        private string _email;
        private string _initials;
        private byte _role_id;
        private string _phone_number;
        private string _password;
        private DateOnly? _birth_date;
        private bool _actuality;

        public ushort ID
        {
            get { return _id; }
            set
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "ID");
                _id = value;
            }
        }

        public string Login
        {
            get { return _login; }
            set
            {  
                FieldValidator.Validate(value, 8, 50, false, "^[a-zA-Z0-9_-]{8,50}$", "логин");
                _login = value;
            }
        }

        public string Email
        {
            get { return _email; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, pattern: "^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", field_name: "email");
                _email = value;
            }
        }

        public string Initials
        {
            get { return _initials; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, pattern: "^[А-ЯЁ][а-яА-ЯёЁ-]* [А-ЯЁ][а-яА-ЯёЁ-]*(| [А-ЯЁ][а-яА-ЯёЁ-]*)$", field_name: "инициалы");
                _initials = value;
            }
        }

        public byte RoleID
        {
            get { return _role_id; }
            set 
            {
                FieldValidator.Validate(value, 1, byte.MaxValue, "role ID");
                _role_id = value;
            }
        }

        public string PhoneNumber
        {
            get { return _phone_number; }
            set
            {
                FieldValidator.Validate(value, 11, 11, true, "^8\\d{10}$", "номер телефона");
                _phone_number = value;
            }
        }
        
        public string Password
        {
            get { return _password; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, field_name: "пароль");
                _password = value;
            }
        }
        
        public DateOnly? BirthDate
        {
            get { return _birth_date; }
            set
            {
                FieldValidator.Validate(value, field_name: "день рождения");
                _birth_date = value;
            }
        }

        public bool Actuality
        {
            get { return _actuality; }
            set { _actuality = value; }
        }

        public User(ushort id, string login, string email, string initials,
                    string phone_number, string password, DateOnly? birth_date,
                    bool actaulity = true, byte role_id = 2)
        {
            ID = id;
            Login = login;
            Email = email;
            Initials = initials;
            PhoneNumber = phone_number;
            Password = password;
            BirthDate = birth_date;
            Actuality = actaulity;
            RoleID = role_id;
        }
    }
}