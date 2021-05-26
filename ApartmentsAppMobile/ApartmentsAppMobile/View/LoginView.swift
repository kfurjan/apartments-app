//
//  LoginView.swift
//  ApartmentsApp
//
//  Created by Kevin Furjan on 24.05.2021.
//

import SwiftUI

struct LoginView: View {
    @State var loginFormState: LoginFormState = .loginForm

    var body: some View {
        GeometryReader { _ in
            VStack(spacing: 30) {
                Image(loginLogo)
                    .resizable()
                    .frame(width: 60, height: 60)
                    .foregroundColor(Color(secondaryColor))

                ZStack {
                    SignUpForm(state: self.$loginFormState)
                        .zIndex(Double(self.loginFormState.rawValue))

                    LoginForm(state: self.$loginFormState)
                }
            }
            .padding(.vertical)
        }
        .background(Color(primaryColor)
        .edgesIgnoringSafeArea(.all))
    }
}

struct LoginView_Previews: PreviewProvider {
    static var previews: some View {
        LoginView()
            .preferredColorScheme(/*@START_MENU_TOKEN@*/.dark/*@END_MENU_TOKEN@*/)
    }
}
