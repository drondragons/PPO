#nullable disable

namespace BLComponent
{
    public class Role
    {
        private byte _id;
        private string _role;

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
            get { return _role; }
            set 
            {
                FieldValidator.Validate(value, _nullable: false, field_name: "роль");
                _role = value;
            }
        }

        public Role(byte id, string name) 
        {
            ID = id;
            Name = name;
        }
    }
}