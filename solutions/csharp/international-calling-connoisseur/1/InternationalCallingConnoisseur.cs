public static class DialingCodes
{
    public static Dictionary<int, string> GetEmptyDictionary()
    {
        return new Dictionary<int,string>();
    }

    public static Dictionary<int, string> GetExistingDictionary()
    {
        Dictionary<int,string> countryCode = new Dictionary<int,string>
        {
            {1, "United States of America"},
            {55, "Brazil"},
            {91,"India"}
        };
        return countryCode;
    }

    public static Dictionary<int, string> AddCountryToEmptyDictionary(int countryCode, string countryName)
    {
        Dictionary<int,string> a =  new Dictionary<int,string> 
        {
            {countryCode, countryName}
        };
        return a;
    }

    public static Dictionary<int, string> AddCountryToExistingDictionary(
        Dictionary<int, string> existingDictionary, int countryCode, string countryName)
    {
        existingDictionary[countryCode] = countryName;
        return existingDictionary;
    }

    public static string GetCountryNameFromDictionary(
        Dictionary<int, string> existingDictionary, int countryCode)
    {
        if(existingDictionary.ContainsKey(countryCode))
            return existingDictionary[countryCode];
        return String.Empty;
    }

    public static bool CheckCodeExists(Dictionary<int, string> existingDictionary, int countryCode)
    {
        return  existingDictionary.ContainsKey(countryCode);
    }

    public static Dictionary<int, string> UpdateDictionary(
        Dictionary<int, string> existingDictionary, int countryCode, string countryName)
    {
        if(existingDictionary.ContainsKey(countryCode))
            existingDictionary[countryCode] = countryName;
            return existingDictionary;
        
        return existingDictionary;
    }

    public static Dictionary<int, string> RemoveCountryFromDictionary(
        Dictionary<int, string> existingDictionary, int countryCode)
    {
        if(existingDictionary.ContainsKey(countryCode))
        {
            existingDictionary.Remove(countryCode);
        }
        return existingDictionary;
    }

    public static string FindLongestCountryName(Dictionary<int, string> existingDictionary)
    {
        string countryWithLongestName = string.Empty;
        foreach (KeyValuePair<int,string> item in existingDictionary)
        {
            if (item.Value.Length > countryWithLongestName.Length)
            {
                countryWithLongestName = item.Value;
            }
        }
        return countryWithLongestName;
    }
}