# dataconnect_generated SDK

## Installation
```sh
flutter pub get firebase_data_connect
flutterfire configure
```
For more information, see [Flutter for Firebase installation documentation](https://firebase.google.com/docs/data-connect/flutter-sdk#use-core).

## Data Connect instance
Each connector creates a static class, with an instance of the `DataConnect` class that can be used to connect to your Data Connect backend and call operations.

### Connecting to the emulator

```dart
String host = 'localhost'; // or your host name
int port = 9399; // or your port number
ExampleConnector.instance.dataConnect.useDataConnectEmulator(host, port);
```

You can also call queries and mutations by using the connector class.
## Queries

### ListProjects
#### Required Arguments
```dart
// No required arguments
ExampleConnector.instance.listProjects().execute();
```



#### Return Type
`execute()` returns a `QueryResult<ListProjectsData, void>`
```dart
/// Result of an Operation Request (query/mutation).
class OperationResult<Data, Variables> {
  OperationResult(this.dataConnect, this.data, this.ref);
  Data data;
  OperationRef<Data, Variables> ref;
  FirebaseDataConnect dataConnect;
}

/// Result of a query request. Created to hold extra variables in the future.
class QueryResult<Data, Variables> extends OperationResult<Data, Variables> {
  QueryResult(super.dataConnect, super.data, super.ref);
}

final result = await ExampleConnector.instance.listProjects();
ListProjectsData data = result.data;
final ref = result.ref;
```

#### Getting the Ref
Each builder returns an `execute` function, which is a helper function that creates a `Ref` object, and executes the underlying operation.
An example of how to use the `Ref` object is shown below:
```dart
final ref = ExampleConnector.instance.listProjects().ref();
ref.execute();

ref.subscribe(...);
```


### ListTeamMembers
#### Required Arguments
```dart
// No required arguments
ExampleConnector.instance.listTeamMembers().execute();
```



#### Return Type
`execute()` returns a `QueryResult<ListTeamMembersData, void>`
```dart
/// Result of an Operation Request (query/mutation).
class OperationResult<Data, Variables> {
  OperationResult(this.dataConnect, this.data, this.ref);
  Data data;
  OperationRef<Data, Variables> ref;
  FirebaseDataConnect dataConnect;
}

/// Result of a query request. Created to hold extra variables in the future.
class QueryResult<Data, Variables> extends OperationResult<Data, Variables> {
  QueryResult(super.dataConnect, super.data, super.ref);
}

final result = await ExampleConnector.instance.listTeamMembers();
ListTeamMembersData data = result.data;
final ref = result.ref;
```

#### Getting the Ref
Each builder returns an `execute` function, which is a helper function that creates a `Ref` object, and executes the underlying operation.
An example of how to use the `Ref` object is shown below:
```dart
final ref = ExampleConnector.instance.listTeamMembers().ref();
ref.execute();

ref.subscribe(...);
```

## Mutations

### CreateInquiry
#### Required Arguments
```dart
String name = ...;
String email = ...;
String message = ...;
ExampleConnector.instance.createInquiry(
  name: name,
  email: email,
  message: message,
).execute();
```

#### Optional Arguments
We return a builder for each query. For CreateInquiry, we created `CreateInquiryBuilder`. For queries and mutations with optional parameters, we return a builder class.
The builder pattern allows Data Connect to distinguish between fields that haven't been set and fields that have been set to null. A field can be set by calling its respective setter method like below:
```dart
class CreateInquiryVariablesBuilder {
  ...
   CreateInquiryVariablesBuilder phoneNumber(String? t) {
   _phoneNumber.value = t;
   return this;
  }
  CreateInquiryVariablesBuilder subject(String? t) {
   _subject.value = t;
   return this;
  }

  ...
}
ExampleConnector.instance.createInquiry(
  name: name,
  email: email,
  message: message,
)
.phoneNumber(phoneNumber)
.subject(subject)
.execute();
```

#### Return Type
`execute()` returns a `OperationResult<CreateInquiryData, CreateInquiryVariables>`
```dart
/// Result of an Operation Request (query/mutation).
class OperationResult<Data, Variables> {
  OperationResult(this.dataConnect, this.data, this.ref);
  Data data;
  OperationRef<Data, Variables> ref;
  FirebaseDataConnect dataConnect;
}

final result = await ExampleConnector.instance.createInquiry(
  name: name,
  email: email,
  message: message,
);
CreateInquiryData data = result.data;
final ref = result.ref;
```

#### Getting the Ref
Each builder returns an `execute` function, which is a helper function that creates a `Ref` object, and executes the underlying operation.
An example of how to use the `Ref` object is shown below:
```dart
String name = ...;
String email = ...;
String message = ...;

final ref = ExampleConnector.instance.createInquiry(
  name: name,
  email: email,
  message: message,
).ref();
ref.execute();
```


### UpdateProjectStatus
#### Required Arguments
```dart
String id = ...;
String status = ...;
ExampleConnector.instance.updateProjectStatus(
  id: id,
  status: status,
).execute();
```



#### Return Type
`execute()` returns a `OperationResult<UpdateProjectStatusData, UpdateProjectStatusVariables>`
```dart
/// Result of an Operation Request (query/mutation).
class OperationResult<Data, Variables> {
  OperationResult(this.dataConnect, this.data, this.ref);
  Data data;
  OperationRef<Data, Variables> ref;
  FirebaseDataConnect dataConnect;
}

final result = await ExampleConnector.instance.updateProjectStatus(
  id: id,
  status: status,
);
UpdateProjectStatusData data = result.data;
final ref = result.ref;
```

#### Getting the Ref
Each builder returns an `execute` function, which is a helper function that creates a `Ref` object, and executes the underlying operation.
An example of how to use the `Ref` object is shown below:
```dart
String id = ...;
String status = ...;

final ref = ExampleConnector.instance.updateProjectStatus(
  id: id,
  status: status,
).ref();
ref.execute();
```

