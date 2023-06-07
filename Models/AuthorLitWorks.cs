#nullable disable

namespace BLComponent
{
    public class AuthorLitWork
    {
        private uint _id;
        private ushort _lit_work_id;
        private ushort _author_id;

        public uint ID
        {
            get { return _id; }
            set 
            {
                FieldValidator.Validate(value, 1, uint.MaxValue, "ID");
                _id = value;
            }
        }

        public ushort LitWorkID
        {
            get { return _lit_work_id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "lit work ID");
                _lit_work_id = value;
            }
        }

        public ushort AuthorID
        {
            get { return _author_id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "author ID");
                _author_id = value;
            }
        }

        public AuthorLitWork(uint id, ushort lit_work_id, ushort author_id)
        {
            ID = id;
            LitWorkID = lit_work_id;
            AuthorID = author_id;
        }
    }
}