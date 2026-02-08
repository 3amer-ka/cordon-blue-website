part of 'generated.dart';

class ListTeamMembersVariablesBuilder {
  final FirebaseDataConnect _dataConnect;
  ListTeamMembersVariablesBuilder(this._dataConnect);
  Deserializer<ListTeamMembersData> dataDeserializer = (dynamic json) =>
      ListTeamMembersData.fromJson(jsonDecode(json));

  Future<QueryResult<ListTeamMembersData, void>> execute() {
    return ref().execute();
  }

  QueryRef<ListTeamMembersData, void> ref() {
    return _dataConnect.query(
      "ListTeamMembers",
      dataDeserializer,
      emptySerializer,
      null,
    );
  }
}

@immutable
class ListTeamMembersTeamMembers {
  final String id;
  final String name;
  final String role;
  final String? photoUrl;
  final String? bio;
  final String? linkedinProfile;
  ListTeamMembersTeamMembers.fromJson(dynamic json)
    : id = nativeFromJson<String>(json['id']),
      name = nativeFromJson<String>(json['name']),
      role = nativeFromJson<String>(json['role']),
      photoUrl = json['photoUrl'] == null
          ? null
          : nativeFromJson<String>(json['photoUrl']),
      bio = json['bio'] == null ? null : nativeFromJson<String>(json['bio']),
      linkedinProfile = json['linkedinProfile'] == null
          ? null
          : nativeFromJson<String>(json['linkedinProfile']);
  @override
  bool operator ==(Object other) {
    if (identical(this, other)) {
      return true;
    }
    if (other.runtimeType != runtimeType) {
      return false;
    }

    final ListTeamMembersTeamMembers otherTyped =
        other as ListTeamMembersTeamMembers;
    return id == otherTyped.id &&
        name == otherTyped.name &&
        role == otherTyped.role &&
        photoUrl == otherTyped.photoUrl &&
        bio == otherTyped.bio &&
        linkedinProfile == otherTyped.linkedinProfile;
  }

  @override
  int get hashCode => Object.hashAll([
    id.hashCode,
    name.hashCode,
    role.hashCode,
    photoUrl.hashCode,
    bio.hashCode,
    linkedinProfile.hashCode,
  ]);

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    json['id'] = nativeToJson<String>(id);
    json['name'] = nativeToJson<String>(name);
    json['role'] = nativeToJson<String>(role);
    if (photoUrl != null) {
      json['photoUrl'] = nativeToJson<String?>(photoUrl);
    }
    if (bio != null) {
      json['bio'] = nativeToJson<String?>(bio);
    }
    if (linkedinProfile != null) {
      json['linkedinProfile'] = nativeToJson<String?>(linkedinProfile);
    }
    return json;
  }

  const ListTeamMembersTeamMembers({
    required this.id,
    required this.name,
    required this.role,
    this.photoUrl,
    this.bio,
    this.linkedinProfile,
  });
}

@immutable
class ListTeamMembersData {
  final List<ListTeamMembersTeamMembers> teamMembers;
  ListTeamMembersData.fromJson(dynamic json)
    : teamMembers = (json['teamMembers'] as List<dynamic>)
          .map((e) => ListTeamMembersTeamMembers.fromJson(e))
          .toList();
  @override
  bool operator ==(Object other) {
    if (identical(this, other)) {
      return true;
    }
    if (other.runtimeType != runtimeType) {
      return false;
    }

    final ListTeamMembersData otherTyped = other as ListTeamMembersData;
    return teamMembers == otherTyped.teamMembers;
  }

  @override
  int get hashCode => teamMembers.hashCode;

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    json['teamMembers'] = teamMembers.map((e) => e.toJson()).toList();
    return json;
  }

  const ListTeamMembersData({required this.teamMembers});
}
