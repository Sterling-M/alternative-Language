using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using System.Linq;

class Program
{
    static void Main()
    {
        
        // Read data from CSV file
       
        Dictionary<int, Cell> data = ReadCSV("cells.csv");
        ;
        List<Cell> cellList = data.Values.ToList();
        // Print transformed data
        foreach (var kvp in data)
        {
            Console.WriteLine($"Index: {kvp.Key}");
            Console.WriteLine(kvp.Value.ToString());
            Console.WriteLine();
            
        }
      
      Cell cell = new Cell();
      float? meanBodyWeight = cell.CalculateMeanBodyWeight(cellList);
      // Check if the meanBodyWeight has a value
      if (meanBodyWeight.HasValue)
      {
          Console.WriteLine($"Mean Body Weight: {meanBodyWeight}");
      }
      else
      {
          Console.WriteLine("No data available to calculate mean body weight.");
      }
      
      
    }

    static Dictionary<int, Cell> ReadCSV(string filePath)
    {
        Dictionary<int, Cell> data = new Dictionary<int, Cell>();
        using (var reader = new StreamReader(filePath))
        {
            string[] headers = reader.ReadLine().Split(',');
            int index = 0;
            while (!reader.EndOfStream)
            {
                string[] values = reader.ReadLine().Split(',');
                Cell cell = new Cell();
                for (int i = 0; i < headers.Length; i++)
                {
                    switch (headers[i])
                    {
                        case "oem":
                            cell.SetOEM(values[i]);
                            break;
                        case "model":
                            cell.SetModel(values[i]);
                            break;
                        case "launch_announced":
                            cell.SetLaunchAnnounced(values[i]);
                            break;
                        case "launch_status":
                            cell.SetLaunchStatus(values[i]);
                            break;
                        case "body_dimensions":
                            cell.SetBodyDimensions(values[i]);
                            break;
                        case "body_weight":
                            cell.SetBodyWeight(values[i]);
                            break;
                        case "body_sim":
                            cell.SetBodySim(values[i]);
                            break;
                        case "display_type":
                            cell.SetDisplayType(values[i]);
                            break;
                        case "display_size":
                            cell.SetDisplaySize(values[i]);
                            break;
                        case "display_resolution":
                            cell.SetDisplayResolution(values[i]);
                            break;
                        case "features_sensors":
                            cell.SetFeaturesSensors(values[i]);
                            break;
                        case "platform_os":
                            cell.SetPlatformOS(values[i]);
                            break;
                    }
                }

                // Apply additional data transformations
                ApplyDataTransformations(cell);

                // Store the cell object in the data structure
                data.Add(index, cell);
                index++;
            }
        }
        return data;
    }

  public static void ApplyDataTransformations(Cell cell)
  {
      // Replace missing or empty values with null
      if (string.IsNullOrWhiteSpace(cell.OEM))
          cell.OEM = null;
      if (string.IsNullOrWhiteSpace(cell.Model))
          cell.Model = null;

      // Transform launch_announced to integer year
      cell.LaunchAnnounced = ExtractYear(cell.LaunchAnnounced?.ToString());

      // Transform launch_status to integer year, or null if "Discontinued" or "Cancelled"
      string launchStatus = cell.LaunchStatus?.ToString();
      if (launchStatus == "Discontinued" || launchStatus == "Cancelled")
      {
          cell.LaunchStatus = null;
      }
      else
      {
          cell.LaunchStatus = ExtractYear(launchStatus);
      }

      // Extract grams from body_weight
      cell.BodyWeight = ExtractGrams(cell.BodyWeight?.ToString());

      // Replace "No" in body_sim with null
      if (cell.BodySim == "No")
      {
          cell.BodySim = null;
      }

      // Shorten platform_os to only include platform name
      cell.PlatformOS = ShortenPlatformOS(cell.PlatformOS);

      // Extract inches from display_size
      cell.DisplaySize = ExtractDisplaySize(cell.DisplaySize?.ToString());
  }

  public static int? ExtractYear(string value)
  {
      if (value == null)
          return null;

      Match match = Regex.Match(value, @"\b\d{4}\b");
      return match.Success ? int.Parse(match.Value) : (int?)null;
  }

  public static float? ExtractGrams(string value)
  {
      if (value == null)
          return null;

      Match match = Regex.Match(value, @"(\d+)\s*g\b");
      if (match.Success)
      {
          if (int.TryParse(match.Groups[1].Value, out int grams))
          {
              return grams;
          }
      }

      return null;
  }

  public static string ShortenPlatformOS(string value)
  {
      if (value == null)
          return null;

      Match match = Regex.Match(value, @"^([^,]+)");
      return match.Success ? match.Groups[1].Value : null;
  }

  public static float? ExtractDisplaySize(string value)
  {
      if (value == null)
          return null;

      Match match = Regex.Match(value, @"([\d.]+)\s*inches\b");
      return match.Success ? float.Parse(match.Groups[1].Value) : (float?)null;
  }


}
class Cell
{
    public string OEM { get; set; }
    public string Model { get; set; }
    public int? LaunchAnnounced { get; set; }
    public int? LaunchStatus { get; set; }
    public string BodyDimensions { get; set; }
    public float? BodyWeight { get; set; }
    public string BodySim { get; set; }
    public string DisplayType { get; set; }
    public float? DisplaySize { get; set; }
    public string DisplayResolution { get; set; }
    public string FeaturesSensors { get; set; }
    public string PlatformOS { get; set; }


    public string GetOEM() { return OEM; }
    public string GetModel() { return Model; }
    public int? GetLaunchAnnounced() { return LaunchAnnounced; }
    public int? GetLaunchStatus() { return LaunchStatus; }
    public string GetBodyDimensions() { return BodyDimensions; }
    public float? GetBodyWeight() { return BodyWeight; }
    public string GetBodySim() { return BodySim; }
    public string GetDisplayType() { return DisplayType; }
    public float? GetDisplaySize() { return DisplaySize; }
    public string GetDisplayResolution() { return DisplayResolution; }
    public string GetFeaturesSensors() { return FeaturesSensors; }
    public string GetPlatformOS() { return PlatformOS; }
    public void SetOEM(string value) { OEM = value; }
    public void SetModel(string value) { Model = value; }
    public void SetLaunchAnnounced(string value) { LaunchAnnounced = Program.ExtractYear(value); }
    public void SetLaunchStatus(string value) { LaunchStatus = value == "Discontinued" || value == "Cancelled" ? null : Program.ExtractYear(value); }
    public void SetBodyDimensions(string value) { BodyDimensions = value; }
    public void SetBodyWeight(string value) { BodyWeight = Program.ExtractGrams(value); }
    public void SetBodySim(string value) { BodySim = value == "No" ? null : value; }
    public void SetDisplayType(string value) { DisplayType = value; }
    public void SetDisplaySize(string value) { DisplaySize = Program.ExtractDisplaySize(value); }
    public void SetDisplayResolution(string value) { DisplayResolution = value; }
    public void SetFeaturesSensors(string value) { FeaturesSensors = value; }
    public void SetPlatformOS(string value) { PlatformOS = Program.ShortenPlatformOS(value); }

  
  
  public override string ToString()
  {
      return $"OEM: {OEM ?? "null"}\n" +
             $"Model: {Model ?? "null"}\n" +
             $"Launch Announced: {LaunchAnnounced}\n" +
             $"Launch Status: {(LaunchStatus.HasValue ? LaunchStatus.ToString() : "null")}\n" +
             $"Body Dimensions: {BodyDimensions ?? "null"}\n" +
             $"Body Weight: {(BodyWeight.HasValue ? BodyWeight.ToString() : "null")}\n" +
             $"Body SIM: {BodySim ?? "null"}\n" +
             $"Display Type: {DisplayType ?? "null"}\n" +
             $"Display Size: {(DisplaySize.HasValue ? DisplaySize.ToString() : "null")}\n" +
             $"Display Resolution: {DisplayResolution ?? "null"}\n" +
             $"Features Sensors: {FeaturesSensors ?? "null"}\n" +
             $"Platform OS: {PlatformOS ?? "null"}";
  }

  public float? CalculateMeanBodyWeight(List<Cell> cells)
  {
      if (cells.Count == 0) return null;

      float sum = 0;
      foreach (var cell in cells)
      {
          if (cell.BodyWeight.HasValue)
              sum += cell.BodyWeight.Value;
      }
    

      return sum / cells.Count;
  }
  
  public List<string> UniqueValues(string column, List<Cell> cells)
  {
      List<string> uniqueValues = new List<string>();
      switch (column)
      {
          case "OEM":
              uniqueValues = cells.Select(c => c.GetOEM()).Where(o => !string.IsNullOrEmpty(o)).Distinct().ToList();
              break;
          case "Model":
              uniqueValues = cells.Select(c => c.GetModel()).Where(m => !string.IsNullOrEmpty(m)).Distinct().ToList();
              break;
          case "LaunchAnnounced":
              uniqueValues = cells.Select(c => c.GetLaunchAnnounced()?.ToString()).Where(l => !string.IsNullOrEmpty(l)).Distinct().ToList();
              break;
          case "LaunchStatus":
              uniqueValues = cells.Select(c => c.GetLaunchStatus()?.ToString()).Where(l => !string.IsNullOrEmpty(l)).Distinct().ToList();
              break;
          case "BodyWeight":
              uniqueValues = cells.Select(c => c.GetBodyWeight()?.ToString()).Where(b => !string.IsNullOrEmpty(b)).Distinct().ToList();
              break;
          case "BodySim":
              uniqueValues = cells.Select(c => c.GetBodySim()).Where(b => !string.IsNullOrEmpty(b)).Distinct().ToList();
              break;
          case "DisplaySize":
              uniqueValues = cells.Select(c => c.GetDisplaySize()?.ToString()).Where(d => !string.IsNullOrEmpty(d)).Distinct().ToList();
              break;
          case "PlatformOS":
              uniqueValues = cells.Select(c => c.GetPlatformOS()).Where(p => !string.IsNullOrEmpty(p)).Distinct().ToList();
              break;
          default:
              break;
      }
      return uniqueValues;
  }



  public void AddObject(string oem, string model, int? launchAnnounced, int? launchStatus, float? bodyWeight, string bodySim, float? displaySize, string platformOS)
  {
      OEM = oem;
      Model = model;
      LaunchAnnounced = launchAnnounced;
      LaunchStatus = launchStatus;
      BodyWeight = bodyWeight;
      BodySim = bodySim;
      DisplaySize = displaySize;
      PlatformOS = platformOS;
  }

 
    public static void DeleteObjectByModel(List<Cell> cells, string model)
    {
        // Find all indexes of objects with the specified model
        List<int> indexesToRemove = new List<int>();
        for (int i = 0; i < cells.Count; i++)
        {
            if (cells[i].GetModel() == model)
            {
                indexesToRemove.Add(i);
            }
        }
    }




  
}
