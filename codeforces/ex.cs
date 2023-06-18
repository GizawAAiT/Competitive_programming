public class Point3D
{
    public double X { get; set; }
    public double Y { get; set; }
    public double Z { get; set; }

    public Point3D(double x, double y, double z)
    {
        X = x;
        Y = y;
        Z = z;
    }

    // ... more code ...
}

public class Program
{
    public static void Main()
    {
        Point3D[] points = new Point3D[]
        {
            new Point3D(2, 3, 4),
            new Point3D(1, 5, 7),
            new Point3D(3, 2, 1),
            new Point3D(1, 2, 3),
        };

        Array.Sort(points, (p1, p2) => {
            int xComparison = p1.X.CompareTo(p2.X);
            if (xComparison == 0)
            {
                return p1.Y.CompareTo(p2.Y);
            }
            return xComparison;
        });

        // Print sorted points
        foreach(var point in points)
        {
            Console.WriteLine($"({point.X}, {point.Y}, {point.Z})");
        }
    }
}