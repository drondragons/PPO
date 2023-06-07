using System.Text.RegularExpressions;
#nullable disable

namespace BLComponent
{
    public class FieldValidator
    {
        public static bool Validate(byte value, string field_name = default)
        {
            return Validate(value, byte.MinValue, byte.MaxValue, field_name);
        }

        public static bool Validate(uint value, string field_name = default)
        {
            return Validate(value, uint.MinValue, uint.MaxValue, field_name);
        }
        
        public static bool Validate(ushort value, string field_name = default)
        {
            return Validate(value, ushort.MinValue, ushort.MaxValue, field_name);
        }

        public static bool Validate(decimal value, string field_name = default)
        {
            return Validate(value, decimal.MinValue, decimal.MaxValue, field_name);
        }

        public static bool Validate(DateTime? value, bool _nullable = true, string field_name = default)
        {
            return Validate(value, default(DateTime), DateTime.Now, _nullable, field_name);
        }

        public static bool Validate(DateOnly? value, bool _nullable = true, string field_name = default)
        {
            return Validate(value, default(DateOnly), DateOnly.FromDateTime(DateTime.Now), _nullable, field_name);
        }

        public static bool Validate(byte value, byte min_value, byte max_value, string field_name = default)
        {
            if (min_value > max_value) throw new ArgumentException("Минимальное значение должно быть меньше максимального!");
            if (value < min_value) throw new ArgumentException($"Поле {field_name} должно быть больше {min_value}!");
            if (value > max_value) throw new ArgumentException($"Поле {field_name} должно быть меньше {max_value}!");
            return true;
        }

        public static bool Validate(uint value, uint min_value, uint max_value, string field_name = default)
        {
            if (min_value > max_value) throw new ArgumentException("Минимальное значение должно быть меньше максимального!");
            if (value < min_value) throw new ArgumentException($"Поле {field_name} должно быть больше {min_value}!");
            if (value > max_value) throw new ArgumentException($"Поле {field_name} должно быть меньше {max_value}!");
            return true;
        }

        public static bool Validate(ushort value, ushort min_value, ushort max_value, string field_name = default)
        {
            if (min_value > max_value) throw new ArgumentException("Минимальное значение должно быть меньше максимального!");
            if (value < min_value) throw new ArgumentException($"Поле {field_name} должно быть больше {min_value}!");
            if (value > max_value) throw new ArgumentException($"Поле {field_name} должно быть меньше {max_value}!");
            return true;
        }

        public static bool Validate(decimal value, decimal min_value, decimal max_value, string field_name = default)
        {
            if (min_value > max_value) throw new ArgumentException("Минимальное значение должно быть меньше максимального!");
            if (value < min_value) throw new ArgumentException($"Поле {field_name} должно быть больше {min_value}!");
            if (value > max_value) throw new ArgumentException($"Поле {field_name} должно быть меньше {max_value}!");
            return true;
        }
    
        public static bool Validate(string value, uint min_length = 0, uint max_length = uint.MaxValue, bool _nullable = true, string pattern = ".*", string field_name = default)
        {
            if (min_length > max_length) throw new ArgumentException("Минимальная длина должна быть меньше максимальной!");
            if (!_nullable && string.IsNullOrWhiteSpace(value)) throw new ArgumentNullException($"Значение поля {field_name} не может быть пустым!");
            if (value != null) 
            {
                if (value.Length < min_length) throw new ArgumentException($"Слишком короткое (меньше {min_length}) значение поля {field_name}!");
                if (value.Length > max_length) throw new ArgumentException($"Слишком длинное (больше {max_length}) значение поля {field_name}!");
                if (!Regex.IsMatch(value, pattern)) throw new ArgumentException($"Значение поля {field_name} не соответствует формату!");
            }
            return true;
        }

        public static bool Validate(DateOnly? value, DateOnly min_date, DateOnly max_date, bool _nullable = true, string field_name = default)
        {
            if (min_date > max_date) throw new ArgumentException("Минимальная дата должна быть меньше максимальной!");
            if (!_nullable && value == null) throw new ArgumentNullException($"Поле {field_name} не может быть null!");
            if (value != null)
            {
                if (value < min_date) throw new ArgumentException($"Слишком ранняя (меньше {min_date}) дата для поля {field_name}!");
                if (value > max_date) throw new ArgumentException($"Слишком поздняя (больше {max_date}) дата для поля {field_name}!");
            }
            return true;
        }

        public static bool Validate(DateTime? value, DateTime min_date, DateTime max_date, bool _nullable = true, string field_name = default)
        {
            if (min_date > max_date) throw new ArgumentException("Минимальная дата должна быть меньше максимальной!");
            if (!_nullable && value == null) throw new ArgumentNullException($"Поле {field_name} не может быть null!");
            if (value != null)
            {
                if (value < min_date) throw new ArgumentException($"Слишком ранняя (меньше {min_date}) дата для поля {field_name}!");
                if (value > max_date) throw new ArgumentException($"Слишком поздняя (больше {max_date}) дата для поля {field_name}!");
            }
            return true;
        }
    }
}


        // public static bool Validate<T>(T value, T minValue, T maxValue, string fieldName = default) 
        // {
        //     if (!IsNumericType(typeof(T)))
        //         throw new ArgumentException($"Полe {fieldName} не может быть типа {typeof(T)}!");
        //     if (Comparer<T>.Default.Compare(maxValue, minValue) < 0)
        //         throw new ArgumentException("Минимальное значение должно быть меньше максимального!");
        //     if (Comparer<T>.Default.Compare(value, minValue) < 0)
        //         throw new ArgumentException($"Поле {fieldName} должно быть больше {minValue}!");
        //     if (Comparer<T>.Default.Compare(value, maxValue) > 0)
        //         throw new ArgumentException($"Поле {fieldName} должно быть меньше {maxValue}!");
        //     return true;
        // }

        // public static bool IsNumericType(Type type)
        // {
        //     if (type == null)
        //         return false;

        //     switch (Type.GetTypeCode(type))
        //     {
        //         case TypeCode.SByte:
        //         case TypeCode.Byte:
        //         case TypeCode.Int16:
        //         case TypeCode.UInt16:
        //         case TypeCode.Int32:
        //         case TypeCode.UInt32:
        //         case TypeCode.Int64:
        //         case TypeCode.UInt64:
        //         case TypeCode.Single:
        //         case TypeCode.Double:
        //         case TypeCode.Decimal:
        //             return true;
        //     }

        //     return false;
        // }