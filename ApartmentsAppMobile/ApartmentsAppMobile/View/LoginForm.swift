//
//  LoginForm.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 25.05.2021.
//

import SwiftUI

struct LoginForm: View {
    @State var email = ""
    @State var password = ""
    @Binding var state: LoginFormState

    var foregroundColor: Color {
        self.state == .loginForm ? .white : .gray
    }

    var capsuleFill: Color {
        self.state == .loginForm ? Color.blue : Color.clear
    }

    var buttonOpacity: Double {
        self.state == .loginForm ? 1 : 0
    }

    var body: some View {
        ZStack(alignment: .bottom) {
            VStack {
                HStack {
                    VStack(spacing: 10) {
                        Text(login)
                            .foregroundColor(foregroundColor)
                            .font(.title)
                            .fontWeight(.bold)
                        Capsule()
                            .fill(capsuleFill)
                            .frame(width: 100, height: 5)
                    }
                    Spacer(minLength: 0)
                }
                .padding(.top, 30)

                VStack {
                    HStack(spacing: 15) {
                        Image(systemName: filledEnvelope)
                        .foregroundColor(Color(secondaryColor))

                        TextField(emailAddressHint, text: self.$email)
                    }
                    Divider().background(Color.white.opacity(0.5))
                }
                .padding(.horizontal)
                .padding(.top, 40)

                VStack {
                    HStack(spacing: 15) {
                        Image(systemName: filledSlashedEye)
                        .foregroundColor(Color(secondaryColor))

                        SecureField(passwordHint, text: self.$password)
                    }
                    Divider().background(Color.white.opacity(0.5))
                }
                .padding(.horizontal)
                .padding(.top, 30)

                HStack {
                    Spacer(minLength: 0)
                    Button(action: {

                    }) {
                        Text(forgotPassword)
                            .foregroundColor(Color.white.opacity(0.6))
                    }
                }
                .padding(.horizontal)
                .padding(.top, 30)
            }
            .padding()
            .padding(.bottom, 65)
            .background(Color(surfaceColor))
            .clipShape(ClipTopRightCorner())
            .contentShape(ClipTopRightCorner())
            .shadow(color: Color.black.opacity(0.3), radius: 5, x: 0, y: -5)
            .onTapGesture {
                self.state = .loginForm
            }
            .cornerRadius(35)
            .padding(.horizontal, 20)

            Button(action: {

            }) {
                Text(login.uppercased())
                    .foregroundColor(.white)
                    .fontWeight(.bold)
                    .padding(.vertical)
                    .padding(.horizontal, 50)
                    .background(Color(secondaryColor))
                    .clipShape(Capsule())
                    .shadow(color: Color.white.opacity(0.1), radius: 5, x: 0, y: 5)
            }
            .offset(y: 25)
            .opacity(buttonOpacity)
        }
    }
}

struct LoginForm_Previews: PreviewProvider {
    static var previews: some View {
        LoginForm(state: .constant(.loginForm))
            .preferredColorScheme(/*@START_MENU_TOKEN@*/.dark/*@END_MENU_TOKEN@*/)
    }
}
