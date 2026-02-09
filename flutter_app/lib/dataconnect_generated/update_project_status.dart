part of 'generated.dart';

class UpdateProjectStatusVariablesBuilder {
  String id;
  String status;

  final FirebaseDataConnect _dataConnect;
  UpdateProjectStatusVariablesBuilder(this._dataConnect, {required  this.id,required  this.status,});
  Deserializer<UpdateProjectStatusData> dataDeserializer = (dynamic json)  => UpdateProjectStatusData.fromJson(jsonDecode(json));
  Serializer<UpdateProjectStatusVariables> varsSerializer = (UpdateProjectStatusVariables vars) => jsonEncode(vars.toJson());
  Future<OperationResult<UpdateProjectStatusData, UpdateProjectStatusVariables>> execute() {
    return ref().execute();
  }

  MutationRef<UpdateProjectStatusData, UpdateProjectStatusVariables> ref() {
    UpdateProjectStatusVariables vars= UpdateProjectStatusVariables(id: id,status: status,);
    return _dataConnect.mutation("UpdateProjectStatus", dataDeserializer, varsSerializer, vars);
  }
}

@immutable
class UpdateProjectStatusProjectUpdate {
  final String id;
  UpdateProjectStatusProjectUpdate.fromJson(dynamic json):
  
  id = nativeFromJson<String>(json['id']);
  @override
  bool operator ==(Object other) {
    if(identical(this, other)) {
      return true;
    }
    if(other.runtimeType != runtimeType) {
      return false;
    }

    final UpdateProjectStatusProjectUpdate otherTyped = other as UpdateProjectStatusProjectUpdate;
    return id == otherTyped.id;
    
  }
  @override
  int get hashCode => id.hashCode;
  

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    json['id'] = nativeToJson<String>(id);
    return json;
  }

  UpdateProjectStatusProjectUpdate({
    required this.id,
  });
}

@immutable
class UpdateProjectStatusData {
  final UpdateProjectStatusProjectUpdate? project_update;
  UpdateProjectStatusData.fromJson(dynamic json):
  
  project_update = json['project_update'] == null ? null : UpdateProjectStatusProjectUpdate.fromJson(json['project_update']);
  @override
  bool operator ==(Object other) {
    if(identical(this, other)) {
      return true;
    }
    if(other.runtimeType != runtimeType) {
      return false;
    }

    final UpdateProjectStatusData otherTyped = other as UpdateProjectStatusData;
    return project_update == otherTyped.project_update;
    
  }
  @override
  int get hashCode => project_update.hashCode;
  

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    if (project_update != null) {
      json['project_update'] = project_update!.toJson();
    }
    return json;
  }

  UpdateProjectStatusData({
    this.project_update,
  });
}

@immutable
class UpdateProjectStatusVariables {
  final String id;
  final String status;
  @Deprecated('fromJson is deprecated for Variable classes as they are no longer required for deserialization.')
  UpdateProjectStatusVariables.fromJson(Map<String, dynamic> json):
  
  id = nativeFromJson<String>(json['id']),
  status = nativeFromJson<String>(json['status']);
  @override
  bool operator ==(Object other) {
    if(identical(this, other)) {
      return true;
    }
    if(other.runtimeType != runtimeType) {
      return false;
    }

    final UpdateProjectStatusVariables otherTyped = other as UpdateProjectStatusVariables;
    return id == otherTyped.id && 
    status == otherTyped.status;
    
  }
  @override
  int get hashCode => Object.hashAll([id.hashCode, status.hashCode]);
  

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    json['id'] = nativeToJson<String>(id);
    json['status'] = nativeToJson<String>(status);
    return json;
  }

  UpdateProjectStatusVariables({
    required this.id,
    required this.status,
  });
}

