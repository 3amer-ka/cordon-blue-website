part of 'generated.dart';

class ListProjectsVariablesBuilder {
  
  final FirebaseDataConnect _dataConnect;
  ListProjectsVariablesBuilder(this._dataConnect, );
  Deserializer<ListProjectsData> dataDeserializer = (dynamic json)  => ListProjectsData.fromJson(jsonDecode(json));
  
  Future<QueryResult<ListProjectsData, void>> execute() {
    return ref().execute();
  }

  QueryRef<ListProjectsData, void> ref() {
    
    return _dataConnect.query("ListProjects", dataDeserializer, emptySerializer, null);
  }
}

@immutable
class ListProjectsProjects {
  final String id;
  final String title;
  final String description;
  final DateTime startDate;
  final DateTime endDate;
  final String status;
  final String? clientName;
  final double? budget;
  final String? location;
  ListProjectsProjects.fromJson(dynamic json):
  
  id = nativeFromJson<String>(json['id']),
  title = nativeFromJson<String>(json['title']),
  description = nativeFromJson<String>(json['description']),
  startDate = nativeFromJson<DateTime>(json['startDate']),
  endDate = nativeFromJson<DateTime>(json['endDate']),
  status = nativeFromJson<String>(json['status']),
  clientName = json['clientName'] == null ? null : nativeFromJson<String>(json['clientName']),
  budget = json['budget'] == null ? null : nativeFromJson<double>(json['budget']),
  location = json['location'] == null ? null : nativeFromJson<String>(json['location']);
  @override
  bool operator ==(Object other) {
    if(identical(this, other)) {
      return true;
    }
    if(other.runtimeType != runtimeType) {
      return false;
    }

    final ListProjectsProjects otherTyped = other as ListProjectsProjects;
    return id == otherTyped.id && 
    title == otherTyped.title && 
    description == otherTyped.description && 
    startDate == otherTyped.startDate && 
    endDate == otherTyped.endDate && 
    status == otherTyped.status && 
    clientName == otherTyped.clientName && 
    budget == otherTyped.budget && 
    location == otherTyped.location;
    
  }
  @override
  int get hashCode => Object.hashAll([id.hashCode, title.hashCode, description.hashCode, startDate.hashCode, endDate.hashCode, status.hashCode, clientName.hashCode, budget.hashCode, location.hashCode]);
  

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    json['id'] = nativeToJson<String>(id);
    json['title'] = nativeToJson<String>(title);
    json['description'] = nativeToJson<String>(description);
    json['startDate'] = nativeToJson<DateTime>(startDate);
    json['endDate'] = nativeToJson<DateTime>(endDate);
    json['status'] = nativeToJson<String>(status);
    if (clientName != null) {
      json['clientName'] = nativeToJson<String?>(clientName);
    }
    if (budget != null) {
      json['budget'] = nativeToJson<double?>(budget);
    }
    if (location != null) {
      json['location'] = nativeToJson<String?>(location);
    }
    return json;
  }

  ListProjectsProjects({
    required this.id,
    required this.title,
    required this.description,
    required this.startDate,
    required this.endDate,
    required this.status,
    this.clientName,
    this.budget,
    this.location,
  });
}

@immutable
class ListProjectsData {
  final List<ListProjectsProjects> projects;
  ListProjectsData.fromJson(dynamic json):
  
  projects = (json['projects'] as List<dynamic>)
        .map((e) => ListProjectsProjects.fromJson(e))
        .toList();
  @override
  bool operator ==(Object other) {
    if(identical(this, other)) {
      return true;
    }
    if(other.runtimeType != runtimeType) {
      return false;
    }

    final ListProjectsData otherTyped = other as ListProjectsData;
    return projects == otherTyped.projects;
    
  }
  @override
  int get hashCode => projects.hashCode;
  

  Map<String, dynamic> toJson() {
    Map<String, dynamic> json = {};
    json['projects'] = projects.map((e) => e.toJson()).toList();
    return json;
  }

  ListProjectsData({
    required this.projects,
  });
}

