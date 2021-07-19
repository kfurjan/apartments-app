//
//  StringConstants.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 25.05.2021.
//

// Colors
let primaryColor = "PrimaryColor"
let secondaryColor = "SecondaryColor"
let surfaceColor = "SurfaceColor"

// UserDefaults keys
let accessTokenKey = "accessToken"
let isUserLoggedInKey = "isUserLoggedIn"

// Logos
let loginLogo = "LoginLogo"

// Strings on UI
let login = "Login"
let signUp = "Sign up"
let emailAddressHint = "Email Address"
let passwordHint = "Password"
let repeatPasswordHint = "Repeat password"
let forgotPassword = "Forget Password?"
let cancel = "Cancel"
let searchPlaceholer = "Search ..."
let apartments = "Apartments"
let available = "Available"
let unavailable = "Unavailable"
let filters = "Filters"
let user = "User"

// System icons
let filledEnvelope = "envelope.fill"
let filledSlashedEye = "eye.slash.fill"
let magnifyingGlass = "magnifyingglass"
let multiplyCircleFill = "multiply.circle.fill"
let locationIconFill = "location.fill"
let euroSignCircleFill = "eurosign.circle.fill"
let checkmark = "checkmark"
let xmark = "xmark"
let starIcon = "star"
let startIconFill = "star.fill"
let filterIcon = "line.horizontal.3.decrease.circle"
let sortIcon = "arrow.up.arrow.down"
let houseIcon = "house"
let personIcon = "person"

// api endpoints
enum ApiConstants {
    static let baseUrl = "http://localhost:8080/api"
    static let apiVersion = "v1"
    static let userApiEndpoint = "\(baseUrl)/\(apiVersion)/user"
    static let loginApiEndpoint = "\(baseUrl)/\(apiVersion)/authentication/login"
    static let apartmentsApiEndpoint = "\(baseUrl)/\(apiVersion)/apartments"
}
