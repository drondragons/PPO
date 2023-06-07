using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class LitWorkGenreTest
    {
        [Theory]
        [InlineData(1, 1, 1)]
        [InlineData(2, 1, 3)]
        public void LitWorkGenre_Creation_PositiveTest(uint id, ushort lit_work_id, ushort genre_id)
        {
            LitWorkGenre Obj = new LitWorkGenre(id, lit_work_id, genre_id);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(lit_work_id, Obj.LitWorkID);
            Assert.Equal(genre_id, Obj.GenreID);
        }

        [Theory]
        [InlineData(0, 1, 1)]
        [InlineData(1, 0, 1)]
        [InlineData(1, 1, 0)]
        public void LitWorkGenre_Creation_ArgumentException_NegativeTest(uint id, ushort lit_work_id, ushort genre_id) 
        {
            Assert.Throws<ArgumentException>(() => new LitWorkGenre(id, lit_work_id, genre_id));
        }
    }
}