//
//  ShapeUtilities.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 25.05.2021.
//

import SwiftUI

struct ClipTopRightCorner: Shape {
    func path(in rectangle: CGRect) -> Path {
        return Path { path in
            path.move(to: CGPoint(x: rectangle.width, y: 100))
            path.addLine(to: CGPoint(x: rectangle.width, y: rectangle.height))
            path.addLine(to: CGPoint(x: 0, y: rectangle.height))
            path.addLine(to: CGPoint(x: 0, y: 0))
        }
    }
}

struct ClipTopLeftCorner: Shape {
    func path(in rectangle: CGRect) -> Path {
        return Path { path in
            path.move(to: CGPoint(x: 0, y: 100))
            path.addLine(to: CGPoint(x: 0, y: rectangle.height))
            path.addLine(to: CGPoint(x: rectangle.width, y: rectangle.height))
            path.addLine(to: CGPoint(x: rectangle.width, y: 0))
        }
    }
}
