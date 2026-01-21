public static class PhoneNumber
{
    public static (bool IsNewYork, bool IsFake, string LocalNumber) Analyze(string phoneNumber)
    {
        string [] allCodes = phoneNumber.Split("-");        
        return (
            String.Equals(allCodes[0],"212",StringComparison.Ordinal),
            String.Equals(allCodes[1],"555",StringComparison.Ordinal),
            allCodes[2]);

    }

    public static bool IsFake((bool IsNewYork, bool IsFake, string LocalNumber) phoneNumberInfo)
    {
        return phoneNumberInfo.IsFake;
    }
}
