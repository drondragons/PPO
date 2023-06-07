#nullable disable

namespace BLComponent
{
    public class BookLitWork
    {
        private uint _id;
        private ushort _book_id;
        private ushort _lit_work_id;

        public uint ID
        {
            get { return _id; }
            set 
            {
                FieldValidator.Validate(value, 1, uint.MaxValue, "ID");
                _id = value;
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

        public ushort LitWorkID
        {
            get { return _lit_work_id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "lit work ID");
                _lit_work_id = value;
            }
        }

        public BookLitWork(uint id, ushort book_id, ushort lit_work_id)
        {
            ID = id;
            BookID = book_id;
            LitWorkID = lit_work_id;
        }
    }
}