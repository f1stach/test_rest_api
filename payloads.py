data_profile = {
                  "uuid": "1234",
                  "login": "login",
                  "email": "example@example.com",
                  "sales_channel_code": "website",
                  "vip_code": "98765",
                  "mobile_phone": "987654321",
                  "vip_agreement": "yes",
                  "personal_data_agreement": "yes",
                  "komputronik_ecommerce_agreement": "yes"
              }

token_number = {
                   "token": "a044966d-837f-4d5d-ae87-91bafc4d5142"
                }

register_user = {
                   "email": "example@example.com",
                   "password": "password",
                   "mobile_phone": "123456789",
                   "vip_agreement": "yes",
                   "personal_data_agreement": "yes",
                   "komputronik_ecommerce_agreement": "yes"
                }

register_user_v3 = {
                   "name": "Homer",
                   "email": "example@example.com",
                   "password": "password",
                   "mobile_phone": "123456789",
                   "city": "Poznan",
                   "birthday": "2000-12-12",
                   "vip_agreement": "yes",
                   "personal_data_agreement": "yes",
                   "komputronik_ecommerce_agreement": "yes"
                }

login_user = {
               "login": "wojtek",
               "password": "wojtek"
            }

change_login_token = {
                       "login": "user",
                       "password": "haslo",
                       "token": "abcd"
                    }

deactivate_user_v1 = {
                       "uuid": "abc123"
                    }

reset_password_v1 = {
                       "login": "user"
                    }

personal_data_update_v3 = {
                           "token": "a044966d-837f-4d5d-ae87-91bafc4d5142",
                           "host": "https://api-komputronik-vippublic.test.netcorner.pl/",
                           "name": "Eryk",
                           "city": "Konin",
                           "birthday": "2000-12-12"
                        }

payload_coupon_v1 = {
                       "items": {
                          "code": "SPORT178064",
                          "code_erp": "",
                          "price_net": 26.748,
                          "price_gross": 32.9,
                          "quantity": 1,
                          "tax_rate": 0.23
                       },
                       "coupon_code": "VIPRABAT20LO0D"
                    }

payload_sales_doc_v1 = {
                           "sales_document_number": "FV123456",
                           "sales_document_amount": "2999.00"
                        }
