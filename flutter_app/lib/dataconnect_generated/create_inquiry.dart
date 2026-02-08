part of 'generated.dart';

class CreateInquiryVariablesBuilder {
  String name;
  String email;
  String message;
  final Optional<String> _phoneNumber = Optional.optional(
    nativeFromJson,
    nativeToJson,
  );
  final Optional<String> _subject = Optional.optional(
    nativeFromJson,
    nativeToJson,
  );

  final FirebaseDataConnect _dataConnect;
  CreateInquiryVariablesBuilder phoneNumber(String? t) {
    _phoneNumber.value = t;
    return this;
  }

  CreateInquiryVariablesBuilder subject(String? t) {
    _subject.value = t;
    return this;
  }

  CreateInquiryVariablesBuilder(
    this._dataConnect, {
    required this.name,
    required this.email,
    required this.message,
  });
  Deserializer<CreateInquiryData> dataDeserializer = (dynamic json) =>
      CreateInquiryData.fromJson(jsonDecode(json));
  Serializer<CreateInquiryVariables> varsSerializer =
      (CreateInquiryVariables vars) => jsonEncode(vars.toJson());
  Future<OperationResult<CreateInquiryData, CreateInquiryVariables>> execute() {
    return ref().execute();
  }

  MutationRef<CreateInquiryData, CreateInquiryVariables> ref() {
    CreateInquiryVariables vars = CreateInquiryVariables(
      name: name,
      email: email,
      message: message,
      phoneNumber: _phoneNumber,
      subject: _subject,
    );
    return _dataConnect.mutation(
      "CreateInquiry",
      dataDeserializer,
      varsSerializer,
      vars,
    );
  }
}

@immutable
class CreateInquiryInquiryInsert {
  final String id;
  CreateInquiryInquiryInsert.fromJson(dynamic json)
    : id = nativeFromJson<String>(json['id']);
  @override
  bool operator ==(Object other) {
    if (identical(this, other)) {
      return true;
    }
    if (other.runtimeType != runtimeType) {
      return false;
    }

    final CreateInquiryInquiryInsert otherTyped =
        other as CreateInquiryInquiryInsert;
    return id == otherTyped.id;
  }

  @override
  int get hashCode => id.hashCode;

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    json['id'] = nativeToJson<String>(id);
    return json;
  }

  const CreateInquiryInquiryInsert({required this.id});
}

@immutable
class CreateInquiryData {
  final CreateInquiryInquiryInsert inquiry_insert;
  CreateInquiryData.fromJson(dynamic json)
    : inquiry_insert = CreateInquiryInquiryInsert.fromJson(
        json['inquiry_insert'],
      );
  @override
  bool operator ==(Object other) {
    if (identical(this, other)) {
      return true;
    }
    if (other.runtimeType != runtimeType) {
      return false;
    }

    final CreateInquiryData otherTyped = other as CreateInquiryData;
    return inquiry_insert == otherTyped.inquiry_insert;
  }

  @override
  int get hashCode => inquiry_insert.hashCode;

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    json['inquiry_insert'] = inquiry_insert.toJson();
    return json;
  }

  const CreateInquiryData({required this.inquiry_insert});
}

@immutable
class CreateInquiryVariables {
  final String name;
  final String email;
  final String message;
  late final Optional<String> phoneNumber;
  late final Optional<String> subject;
  @Deprecated(
    'fromJson is deprecated for Variable classes as they are no longer required for deserialization.',
  )
  CreateInquiryVariables.fromJson(Map<String, dynamic> json)
    : name = nativeFromJson<String>(json['name']),
      email = nativeFromJson<String>(json['email']),
      message = nativeFromJson<String>(json['message']) {
    phoneNumber = Optional.optional(nativeFromJson, nativeToJson);
    phoneNumber.value = json['phoneNumber'] == null
        ? null
        : nativeFromJson<String>(json['phoneNumber']);

    subject = Optional.optional(nativeFromJson, nativeToJson);
    subject.value = json['subject'] == null
        ? null
        : nativeFromJson<String>(json['subject']);
  }
  @override
  bool operator ==(Object other) {
    if (identical(this, other)) {
      return true;
    }
    if (other.runtimeType != runtimeType) {
      return false;
    }

    final CreateInquiryVariables otherTyped = other as CreateInquiryVariables;
    return name == otherTyped.name &&
        email == otherTyped.email &&
        message == otherTyped.message &&
        phoneNumber == otherTyped.phoneNumber &&
        subject == otherTyped.subject;
  }

  @override
  int get hashCode => Object.hashAll([
    name.hashCode,
    email.hashCode,
    message.hashCode,
    phoneNumber.hashCode,
    subject.hashCode,
  ]);

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    json['name'] = nativeToJson<String>(name);
    json['email'] = nativeToJson<String>(email);
    json['message'] = nativeToJson<String>(message);
    if (phoneNumber.state == OptionalState.set) {
      json['phoneNumber'] = phoneNumber.toJson();
    }
    if (subject.state == OptionalState.set) {
      json['subject'] = subject.toJson();
    }
    return json;
  }

  CreateInquiryVariables({
    required this.name,
    required this.email,
    required this.message,
    required this.phoneNumber,
    required this.subject,
  });
}
