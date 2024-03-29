﻿using System;
using System.Drawing;
using System.Drawing.Graphics;

namespace COMP4106_A3
{
    class A3
    {
        private void DrawImagePointF(PaintEventArgs e)
        {
                    
            // Create image.
            Image newImage = Image.FromFile("SampImag.jpg");
                    
            // Create point for upper-left corner of image.
            PointF ulCorner = new PointF(100.0F, 100.0F);
                    
            // Draw image to screen.
            e.Graphics.DrawImage(newImage, ulCorner);
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
