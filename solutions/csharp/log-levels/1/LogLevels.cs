using System;
using System.Text.RegularExpressions;
static class LogLine
{
    public static string Message(string logLine)
    {
        return logLine.Split(':')[1].Trim();
    }

    public static string LogLevel(string logLine)
    {
        string text = logLine.Split(':')[0].Trim();
        string inside =  text.Replace("[", "").Replace("]", "");
        return inside.ToLowerInvariant();
    }

    public static string Reformat(string logLine)
    {
        string logLevel = logLine.Split(':')[0].Trim().Replace("[", "").Replace("]", "").ToLowerInvariant();
        string logline = logLine.Split(':')[1].Trim();
        return $"{logline} ({logLevel })";
    }
}
// Refactored code 
/*
using System;
using System.Text.RegularExpressions;

static class LogLine
{
    public static string Message(string logLine) =>
        GetMessage(logLine);

    public static string LogLevel(string logLine) =>
        GetLogLevel(logLine);

    public static string Reformat(string logLine) =>
        $"{GetMessage(logLine)} ({GetLogLevel(logLine)})";

    // --- Private helpers ---
    private static string GetMessage(string logLine)
    {
        int colonIndex = logLine.IndexOf(':');
        return logLine.Substring(colonIndex + 1).Trim();
    }

    private static string GetLogLevel(string logLine)
    {
        int colonIndex = logLine.IndexOf(':');
        string level = logLine.Substring(0, colonIndex).Trim();
        return level.Trim('[', ']').ToLowerInvariant();
    }
}

*/
