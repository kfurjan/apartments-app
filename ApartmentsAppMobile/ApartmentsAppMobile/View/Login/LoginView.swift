//
//  LoginView.swift
//  ApartmentsApp
//
//  Created by Kevin Furjan on 24.05.2021.
//

import SwiftUI

struct LoginView: View {

    @StateObject var model = LoginViewModel()

    var body: some View {
        GeometryReader { _ in
            VStack(spacing: 30) {
                Image(loginLogo)
                    .resizable()
                    .frame(width: 60, height: 60)
                    .foregroundColor(Color(secondaryColor))

                ZStack {
                    SignUpForm()
                        .zIndex(Double(self.model.formModel.formState.rawValue))

                    LoginForm()
                }
            }
            .padding(.vertical)
        }
        .background(Color(primaryColor)
        .edgesIgnoringSafeArea(.all))
        .environmentObject(model)
    }
}

struct LoginView_Previews: PreviewProvider {
    static var previews: some View {
        LoginView()
            .preferredColorScheme(/*@START_MENU_TOKEN@*/.dark/*@END_MENU_TOKEN@*/)
    }
}
