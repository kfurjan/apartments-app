//
//  SignUpForm.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 25.05.2021.
//

import SwiftUI

struct SignUpForm: View {
    @EnvironmentObject private var model: LoginViewModel

    private var foregroundColor: Color {
        model.getFormState() == .signUpForm ? .white : .gray
    }
    private var capsuleFill: Color {
        model.getFormState() == .signUpForm ? Color.blue : Color.clear
    }
    private var buttonOpacity: Double {
        model.getFormState() == .signUpForm ? 1 : 0
    }

    var body: some View {
        ZStack(alignment: .bottom) {
            VStack {
                HStack {
                    Spacer(minLength: 0)
                    VStack(spacing: 10) {
                        Text(signUp)
                            .foregroundColor(foregroundColor)
                            .font(.title)
                            .fontWeight(.bold)

                        Capsule()
                            .fill(capsuleFill)
                            .frame(width: 100, height: 5)
                    }
                }
                .padding(.top, 30)

                VStack {
                    HStack(spacing: 15) {
                        Image(systemName: filledEnvelope)
                        .foregroundColor(Color(secondaryColor))

                        TextField(emailAddressHint, text: $model.formModel.email)
                    }
                    Divider().background(Color.white.opacity(0.5))
                }
                .padding(.horizontal)
                .padding(.top, 40)

                VStack {
                    HStack(spacing: 15) {
                        Image(systemName: filledSlashedEye)
                        .foregroundColor(Color(secondaryColor))

                        SecureField(passwordHint, text: $model.formModel.password)
                    }
                    Divider().background(Color.white.opacity(0.5))
                }
                .padding(.horizontal)
                .padding(.top, 30)

                VStack {
                    HStack(spacing: 15) {
                        Image(systemName: filledSlashedEye)
                        .foregroundColor(Color(secondaryColor))

                        SecureField(passwordHint, text: $model.formModel.repeatPassword)
                    }
                    Divider().background(Color.white.opacity(0.5))
                }
                .padding(.horizontal)
                .padding(.top, 30)
            }
            .padding()
            .padding(.bottom, 65)
            .background(Color(surfaceColor))
            .clipShape(ClipTopLeftCorner())
            .contentShape(ClipTopLeftCorner())
            .shadow(color: Color.black.opacity(0.3), radius: 5, x: 0, y: -5)
            .onTapGesture {
                model.setFormState(formState: .signUpForm)
            }
            .cornerRadius(35)
            .padding(.horizontal, 20)

            Button(action: {

            }) {
                Text(signUp.uppercased())
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
        .onChange(of: model.formModel.formState, perform: { _ in
            model.cleanUp()
        })
    }
}

struct SignUpForm_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            SignUpForm()
                .preferredColorScheme(/*@START_MENU_TOKEN@*/.dark/*@END_MENU_TOKEN@*/)
                .environmentObject(LoginViewModel(isPreview: true))
                .previewDisplayName("On focus")

            SignUpForm()
                .preferredColorScheme(/*@START_MENU_TOKEN@*/.dark/*@END_MENU_TOKEN@*/)
                .environmentObject(LoginViewModel(isPreview: false))
                .previewDisplayName("Out of focus")
        }
    }
}
