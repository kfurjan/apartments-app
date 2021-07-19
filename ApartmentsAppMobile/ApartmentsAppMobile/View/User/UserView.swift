//
//  UserView.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 15.07.2021.
//

import SwiftUI

struct UserRowView: View {

    let user: User

    var body: some View {
        HStack {
            Image(systemName: personIcon)
                .resizable()
                .foregroundColor(Color(secondaryColor))
                .frame(width: 100, height: 100, alignment: .center)

            Spacer()

            VStack {
                HStack {
                    Text(user.role.rawValue.capitalized)
                        .bold()
                        .font(.title)
                    Spacer()
                }
                .padding(.bottom, 10)
                .padding(.horizontal, 20)

                HStack {
                    Text(user.email)
                        .bold()
                        .font(.headline)
                    Spacer()
                }
                .padding(.top, 10)
                .padding(.horizontal, 20)

                Spacer()
            }
            .padding()
        }
        .padding()
        .frame(height: 150, alignment: .center)
        .cornerRadius(.infinity)
        .background(Color(surfaceColor))
    }
}

struct UserView: View {

    @EnvironmentObject var appViewModel: AppViewModel

    var body: some View {
        VStack {
            UserRowView(user: appViewModel.user)
            Spacer()

            Button(action: {
                appViewModel.logOutUser()
            }) {
                Spacer()
                Text("Log out")
                    .font(.title2)
                    .padding()
                    .foregroundColor(.white)
                Spacer()
            }
            .background(Color(secondaryColor))
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .padding()

            Spacer()
        }
        .padding(.top, 30)
        .padding(.horizontal)
        .background(Color(primaryColor).edgesIgnoringSafeArea(.all))
        .navigate(to: LoginView()
                    .preferredColorScheme(.dark),
                  when: $appViewModel.isUserLoggedOut)
    }
}

struct UserView_Previews: PreviewProvider {
    static var previews: some View {
        UserView()
            .preferredColorScheme(.dark)
            .environmentObject(AppViewModel(isPreview: true))
    }
}
