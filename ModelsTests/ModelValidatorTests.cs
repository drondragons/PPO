using Xunit;
using BLComponent;
#nullable disable

namespace BLModelTests
{
    public class FieldValidatorTest
    {
        [Theory]
        [InlineData(byte.MinValue, default)]
        [InlineData(byte.MaxValue, default)]
        [InlineData((byte.MaxValue - byte.MinValue) / 2, "Field2")]
        public void Validate_ByteValue_PositiveTest(byte value, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, field_name));
        }

        [Theory]
        [InlineData(0, 0, 100, default)]
        [InlineData(10, 0, 100, default)]
        [InlineData(100, 0, 100, default)]
        public void Validate_IntervalByteValue_PositiveTest(byte value, byte min_value, byte max_value, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, min_value, max_value, field_name));
        }

        [Theory]
        [InlineData(0, 1, 100, default)]
        [InlineData(10, 100, 0, default)]
        [InlineData(101, 0, 100, default)]
        public void Validate_ByteValue_NegativeTest(byte value, byte min_value, byte max_value, string field_name)
        {
            Assert.Throws<ArgumentException>(() => FieldValidator.Validate(value, min_value, max_value, field_name));
        }



        [Theory]
        [InlineData(ushort.MinValue, default)]
        [InlineData(ushort.MaxValue, default)]
        [InlineData((ushort.MaxValue - ushort.MinValue) / 2, "Field2")]
        public void Validate_UshortValue_PositiveTest(ushort value, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, field_name));
        }

        [Theory]
        [InlineData(0, 0, 100, default)]
        [InlineData(10, 0, 100, default)]
        [InlineData(100, 0, 100, default)]
        public void Validate_IntervalUshortValue_PositiveTest(ushort value, ushort min_value, ushort max_value, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, min_value, max_value, field_name));
        }

        [Theory]
        [InlineData(0, 1, 100, default)]
        [InlineData(10, 100, 0, default)]
        [InlineData(101, 0, 100, default)]
        public void Validate_UshortValue_NegativeTest(ushort value, ushort min_value, ushort max_value, string field_name)
        {
            Assert.Throws<ArgumentException>(() => FieldValidator.Validate(value, min_value, max_value, field_name));
        }



        [Theory]
        [InlineData(uint.MinValue, default)]
        [InlineData(uint.MaxValue, default)]
        [InlineData((uint.MaxValue - uint.MinValue) / 2, "Field2")]
        public void Validate_UintValue_PositiveTest(uint value, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, field_name));
        }

        [Theory]
        [InlineData(0, 0, 100, default)]
        [InlineData(10, 0, 100, default)]
        [InlineData(100, 0, 100, default)]
        public void Validate_IntervalUintValue_PositiveTest(uint value, uint min_value, uint max_value, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, min_value, max_value, field_name));
        }

        [Theory]
        [InlineData(0, 1, 100, default)]
        [InlineData(10, 100, 0, default)]
        [InlineData(101, 0, 100, default)]
        public void Validate_UintValue_NegativeTest(uint value, uint min_value, uint max_value, string field_name)
        {
            Assert.Throws<ArgumentException>(() => FieldValidator.Validate(value, min_value, max_value, field_name));
        }



        public static IEnumerable<object[]> TestCorrectDecimalValidation
        {
            get
            {
                yield return new object[] { decimal.MinValue, default };
                yield return new object[] { decimal.MaxValue, default };
                yield return new object[] { default(decimal), "Field2" };
            }
        }

        public static IEnumerable<object[]> TestCorrectIntervalDecimalValidation
        {
            get
            {
                yield return new object[] { decimal.MinValue, decimal.MinValue, decimal.MaxValue, default };
                yield return new object[] { decimal.MaxValue, decimal.MinValue, decimal.MaxValue, default };
                yield return new object[] { default(decimal), decimal.MinValue, decimal.MaxValue, "Field2" };
            }
        }

        public static IEnumerable<object[]> TestDecimalWrongIntervalValidation
        {
            get
            {
                yield return new object[] { decimal.MinValue, default(decimal), decimal.MaxValue, default };
                yield return new object[] { decimal.MaxValue, decimal.MinValue, default(decimal), default };
                yield return new object[] { default(decimal), decimal.MaxValue, decimal.MinValue, "Field2" };
            }
        }

        [Theory]
        [MemberData(nameof(TestCorrectDecimalValidation))]
        public void Validate_DecimalValue_PositiveTest(decimal value, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, field_name));
        }

        [Theory]
        [MemberData(nameof(TestCorrectIntervalDecimalValidation))]
        public void Validate_IntervalDecimalValue_PositiveTest(decimal value, decimal min_value, decimal max_value, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, min_value, max_value, field_name));
        }

        [Theory]
        [MemberData(nameof(TestDecimalWrongIntervalValidation))]
        public void Validate_IntervalDecimalValue_NegativeTest(decimal value, decimal min_value, decimal max_value, string field_name)
        {
            Assert.Throws<ArgumentException>(() => FieldValidator.Validate(value, min_value, max_value, field_name));
        }

        

        [Theory]
        [InlineData("Привет", 6, 6, false, ".*", null)]
        [InlineData(null, 10, 12, true, "^[a-zA-Z0-9_-]{8,50}$", null)]
        [InlineData("HelloWorld", 1, 100, true, "^[a-zA-Z0-9_-]{8,50}$", null)]
        public void Validate_StringValue_PositiveTest(string value, uint min_length, uint max_length, bool _nullable, string pattern, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, min_length, max_length, _nullable, pattern, field_name));
        }

        [Theory]
        [InlineData("", 0, 100, false, "^[a-zA-Z0-9_-]{8,50}$", null)]
        [InlineData(null, 0, 100, false, "^[a-zA-Z0-9_-]{8,50}$", null)]
        [InlineData("   ", 0, 100, false, "^[a-zA-Z0-9_-]{8,50}$", null)]
        public void Validate_StringNullValue_NegativeTest(string value, uint min_length, uint max_length, bool _nullable, string pattern, string field_name)
        {
            Assert.Throws<ArgumentNullException>(() => FieldValidator.Validate(value, min_length, max_length, _nullable, pattern, field_name));
        }

        [Theory]
        [InlineData("Привет", 1, 5, false, ".*", null)]
        [InlineData("Привет", 7, 50, false, ".*", null)]
        [InlineData("Привет", 10, 5, false, ".*", null)]
        [InlineData("HelloWorld", 8, 50, false, "^[a-zA-Z0-9_-]{11,50}$", null)]
        [InlineData("Привет Всем", 8, 50, false, "^[a-zA-Z0-9_-]{8,50}$", null)]
        public void Validate_StringValue_NegativeTest(string value, uint min_length, uint max_length, bool _nullable, string pattern, string field_name)
        {
            Assert.Throws<ArgumentException>(() => FieldValidator.Validate(value, min_length, max_length, _nullable, pattern, field_name));
        }



        public static IEnumerable<object[]> TestCorrectDateOnlyValidation
        {
            get
            {
                yield return new object[] { null, true, null };
                yield return new object[] { new DateOnly(2000, 1, 1), true, null };
                yield return new object[] { new DateOnly(2000, 1, 1), false, null };
            }
        }

        public static IEnumerable<object[]> TestNullDateValidation
        {
            get
            {
                yield return new object[] { null, false, null };
            }
        }

        public static IEnumerable<object[]> TestCorrectDateOnlyIntervalValidation 
        {
            get
            {
                yield return new object[] { null, default(DateOnly), DateOnly.FromDateTime(DateTime.Now), true, null };
                yield return new object[] { new DateOnly(2000, 1, 1), new DateOnly(1999, 12, 31), new DateOnly(2000, 1, 2), true, null };
                yield return new object[] { new DateOnly(2000, 1, 1), default(DateOnly), DateOnly.FromDateTime(DateTime.Now), false, null };
            }
        }

        public static IEnumerable<object[]> TestNullDateOnlyIntervalValidation
        {
            get
            {
                yield return new object[] { null, default(DateOnly), DateOnly.FromDateTime(DateTime.Now), false, null };
            }
        }

        public static IEnumerable<object[]> TestDatOnlyWrongIntervalValidation
        {
            get
            {
                yield return new object[] { null, DateOnly.FromDateTime(DateTime.Now), default(DateOnly), true, null};
                yield return new object[] { new DateOnly(2000, 1, 1), new DateOnly(2000, 1, 2), new DateOnly(2000, 1, 3), false, null};
                yield return new object[] { new DateOnly(2000, 1, 1), new DateOnly(1999, 1, 1), new DateOnly(1999, 12, 31), false, null};
            }
        }

        [Theory]
        [MemberData(nameof(TestCorrectDateOnlyValidation))]
        public void Validate_DateOnlyValue_PositiveTest(DateOnly? value, bool _nullable, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, _nullable, field_name));
        }

        [Theory]
        [MemberData(nameof(TestNullDateValidation))]
        public void Validate_DateOnlyNullValue_NegativeTest(DateOnly? value, bool _nullable, string field_name)
        {
            Assert.Throws<ArgumentNullException>(() => FieldValidator.Validate(value, _nullable, field_name));
        }

        [Theory]
        [MemberData(nameof(TestCorrectDateOnlyIntervalValidation))]
        public void Validate_DateOnlyIntervalValue_PositiveTest(DateOnly? value, DateOnly min_date, DateOnly max_date, bool _nullable, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, min_date, max_date, _nullable, field_name));
        }

        [Theory]
        [MemberData(nameof(TestNullDateOnlyIntervalValidation))]
        public void Validate_DateOnlyIntervalNullValue_NegativeTest(DateOnly? value, DateOnly min_date, DateOnly max_date, bool _nullable, string field_name)
        {
            Assert.Throws<ArgumentNullException>(() => FieldValidator.Validate(value, min_date, max_date, _nullable, field_name));
        }

        [Theory]
        [MemberData(nameof(TestDatOnlyWrongIntervalValidation))]
        public void Validate_DateOnlyWrongInterval_NegativeTest(DateOnly? value, DateOnly min_date, DateOnly max_date, bool _nullable, string field_name)
        {
            Assert.Throws<ArgumentException>(() => FieldValidator.Validate(value, min_date, max_date, _nullable, field_name));
        }





        public static IEnumerable<object[]> TestCorrectDateTimeValidation
        {
            get
            {
                yield return new object[] { null, true, null };
                yield return new object[] { new DateTime(2000, 1, 1, 10, 0, 0), true, null };
                yield return new object[] { new DateTime(2000, 1, 1, 10, 0, 0), false, null };
            }
        }

        public static IEnumerable<object[]> TestCorrectDateTimeIntervalValidation 
        {
            get
            {
                yield return new object[] { null, default(DateTime), DateTime.Now, true, null };
                yield return new object[] { new DateTime(2000, 1, 1, 10, 0, 0), new DateTime(1999, 12, 31, 10, 0, 0), new DateTime(2000, 1, 2, 10, 0, 0), true, null };
                yield return new object[] { new DateTime(2000, 1, 1, 10, 0, 0), default(DateTime), DateTime.Now, false, null };
            }
        }

        public static IEnumerable<object[]> TestNullDateTimeIntervalValidation
        {
            get
            {
                yield return new object[] { null, default(DateTime), DateTime.Now, false, null };
            }
        }

        public static IEnumerable<object[]> TestDateTimeWrongIntervalValidation
        {
            get
            {
                yield return new object[] { null, DateTime.Now, default(DateTime), true, null};
                yield return new object[] { new DateTime(2000, 1, 1, 10, 0, 0), new DateTime(2000, 1, 2, 10, 0, 0), new DateTime(2000, 1, 3, 10, 0, 0), false, null};
                yield return new object[] { new DateTime(2000, 1, 1, 10, 0, 0), new DateTime(1999, 1, 1, 10, 0, 0), new DateTime(1999, 12, 31, 10, 0, 0), false, null};
            }
        }

        [Theory]
        [MemberData(nameof(TestCorrectDateTimeValidation))]
        public void Validate_DateTimeValue_PositiveTest(DateTime? value, bool _nullable, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, _nullable, field_name));
        }

        [Theory]
        [MemberData(nameof(TestNullDateValidation))]
        public void Validate_DateTimeNullValue_NegativeTest(DateTime? value, bool _nullable, string field_name)
        {
            Assert.Throws<ArgumentNullException>(() => FieldValidator.Validate(value, _nullable, field_name));
        }

        [Theory]
        [MemberData(nameof(TestCorrectDateTimeIntervalValidation))]
        public void Validate_DateTimeIntervalValue_PositiveTest(DateTime? value, DateTime min_date, DateTime max_date, bool _nullable, string field_name)
        {
            Assert.True(FieldValidator.Validate(value, min_date, max_date, _nullable, field_name));
        }

        [Theory]
        [MemberData(nameof(TestNullDateTimeIntervalValidation))]
        public void Validate_DateTimeIntervalNullValue_NegativeTest(DateTime? value, DateTime min_date, DateTime max_date, bool _nullable, string field_name)
        {
            Assert.Throws<ArgumentNullException>(() => FieldValidator.Validate(value, min_date, max_date, _nullable, field_name));
        }

        [Theory]
        [MemberData(nameof(TestDateTimeWrongIntervalValidation))]
        public void Validate_DateTimeWrongInterval_NegativeTest(DateTime? value, DateTime min_date, DateTime max_date, bool _nullable, string field_name)
        {
            Assert.Throws<ArgumentException>(() => FieldValidator.Validate(value, min_date, max_date, _nullable, field_name));
        }

    }
}

        // [Theory]
        // [InlineData(typeof(sbyte), true)]
        // [InlineData(typeof(byte), true)]
        // [InlineData(typeof(Int16), true)]
        // [InlineData(typeof(Int32), true)]
        // [InlineData(typeof(Int64), true)]
        // [InlineData(typeof(UInt16), true)]
        // [InlineData(typeof(UInt32), true)]
        // [InlineData(typeof(UInt64), true)]
        // [InlineData(typeof(Single), true)]
        // [InlineData(typeof(Double), true)]
        // [InlineData(typeof(Decimal), true)]
        // [InlineData(null, false)]
        // [InlineData(typeof(char), false)]
        // [InlineData(typeof(string), false)]
        // [InlineData(typeof(bool), false)]
        // [InlineData(typeof(DateTime), false)]
        // [InlineData(typeof(byte[]), false)]
        // public void IsNumericType_ReturnExpectedResult(Type type, bool result)
        // {
        //     Assert.Equal(result, FieldValidator.IsNumericType(type));
        // }


        // [Theory]
        // [InlineData(-1, -2, 0, null)]
        // [InlineData(0, 0, 0, "ikvsndvn")]
        // [InlineData(0.5, -0.5, 0.5, "")]
        // public void Validate_Success_NumericTypes<T>(T value, T minValue, T maxValue, string fieldName)
        // {
        //     Assert.True(FieldValidator.Validate(value, minValue, maxValue, fieldName));
        // }

        // [Theory]
        // [InlineData(' ', 0, 0, null)]
        // [InlineData("", 0, 0, null)]
        // [InlineData("     ", 0, 0, null)]
        // [InlineData(true, 0, 0, null)]
        // [InlineData(false, 0, 0, null)]
        // public void Validate_TypeException<T>(T value, T minValue, T maxValue, string fieldName)
        // {
        //     Assert.Throws<ArgumentException>(() => FieldValidator.Validate(value, minValue, maxValue, fieldName));
        // }

        // [Theory]
        // [InlineData(-1, 1, 10, null)]
        // [InlineData(0.99, 1, 10, null)]
        // [InlineData(11, 1, 10, null)]
        // [InlineData(10, 10, 1, null)]
        // public void Validate_Interval_Exception<T>(T value, T minValue, T maxValue, string fieldName)
        // {
        //     Assert.Throws<ArgumentException>(() => FieldValidator.Validate(value, minValue, maxValue, fieldName));
        // }