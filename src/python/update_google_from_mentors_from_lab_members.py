import argparse
import yaml
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define the scopes required
SCOPES = ["https://www.googleapis.com/auth/forms.body"]


def authenticate_with_service_account(service_account_file):
    """Authenticate with the Google Forms API using a service account."""
    credentials = service_account.Credentials.from_service_account_file(
        service_account_file, scopes=SCOPES
    )
    service = build("forms", "v1", credentials=credentials)
    return service


def load_yaml_data(yaml_file_path):
    """Load data from a YAML file."""
    with open(yaml_file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def update_form_item(service, form_id, item_id, data):
    """Update the form item with new options based on the YAML data."""
    # Extract relevant information and sort it
    options = [name for name, info in data.items() if info["role"] in ["Master", "PhD"]]
    options.sort()
    options += ["I won't need mentorship."]

    # Prepare the update request
    update_request_body = {
        "requests": [
            {
                "updateItem": {
                    "item": {
                        "itemId": item_id,
                        "questionItem": {
                            "question": {
                                "choiceQuestion": {
                                    "options": [{"value": name} for name in options]
                                }
                            }
                        },
                    },
                    "updateMask": "questionItem.question.choiceQuestion.options",
                }
            }
        ]
    }

    # Execute the update request
    response = (
        service.forms().batchUpdate(formId=form_id, body=update_request_body).execute()
    )
    print("Form item updated:", response)


def main():
    parser = argparse.ArgumentParser(
        description="Update a Google Form item based on YAML data."
    )
    parser.add_argument(
        "service_account_file", help="Path to the service account credentials file."
    )
    parser.add_argument("yaml_file_path", help="Path to the YAML file containing data.")
    parser.add_argument("form_id", help="ID of the Google Form to update.")
    parser.add_argument("item_id", help="ID of the form item to update.")

    args = parser.parse_args()

    service = authenticate_with_service_account(args.service_account_file)
    data = load_yaml_data(args.yaml_file_path)
    update_form_item(service, args.form_id, args.item_id, data)


if __name__ == "__main__":
    main()
