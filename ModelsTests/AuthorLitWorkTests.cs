using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class AuthorLitWorkTest
    {
        [Theory]
        [InlineData(1, 1, 1)]
        [InlineData(2, 1, 3)]
        public void AuthorLitWork_Creation_PositiveTest(uint id, ushort lit_work_id, ushort author_id)
        {
            AuthorLitWork Obj = new AuthorLitWork(id, lit_work_id, author_id);

            Assert.Equal(id, Obj.ID);
            Assert.Equal(lit_work_id, Obj.LitWorkID);
            Assert.Equal(author_id, Obj.AuthorID);
        }

        [Theory]
        [InlineData(0, 1, 1)]
        [InlineData(1, 0, 1)]
        [InlineData(1, 1, 0)]
        public void AuthorLitWork_Creation_ArgumentException_NegativeTest(uint id, ushort lit_work_id, ushort author_id) 
        {
            Assert.Throws<ArgumentException>(() => new AuthorLitWork(id, lit_work_id, author_id));
        }
    }
}