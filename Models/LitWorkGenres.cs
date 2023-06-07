#nullable disable

namespace BLComponent
{
    public class LitWorkGenre
    {
        private uint _id;
        private ushort _lit_work_id;
        private ushort _genre_id;

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

        public ushort GenreID
        {
            get { return _genre_id; }
            set 
            {
                FieldValidator.Validate(value, 1, ushort.MaxValue, "genre ID");
                _genre_id = value;
            }
        }

        public LitWorkGenre(uint id, ushort lit_work_id, ushort genre_id)
        {
            ID = id;
            LitWorkID = lit_work_id;
            GenreID = genre_id;
        }
    }
}