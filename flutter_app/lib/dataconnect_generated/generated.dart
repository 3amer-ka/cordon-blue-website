library dataconnect_generated;
import 'package:firebase_data_connect/firebase_data_connect.dart';
import 'package:flutter/foundation.dart';
import 'dart:convert';

part 'create_inquiry.dart';

part 'list_projects.dart';

part 'update_project_status.dart';

part 'list_team_members.dart';







class ExampleConnector {
  
  
  CreateInquiryVariablesBuilder createInquiry ({required String name, required String email, required String message, }) {
    return CreateInquiryVariablesBuilder(dataConnect, name: name,email: email,message: message,);
  }
  
  
  ListProjectsVariablesBuilder listProjects () {
    return ListProjectsVariablesBuilder(dataConnect, );
  }
  
  
  UpdateProjectStatusVariablesBuilder updateProjectStatus ({required String id, required String status, }) {
    return UpdateProjectStatusVariablesBuilder(dataConnect, id: id,status: status,);
  }
  
  
  ListTeamMembersVariablesBuilder listTeamMembers () {
    return ListTeamMembersVariablesBuilder(dataConnect, );
  }
  

  static ConnectorConfig connectorConfig = ConnectorConfig(
    'us-east4',
    'example',
    'cordon-blue-website',
  );

  ExampleConnector({required this.dataConnect});
  static ExampleConnector get instance {
    return ExampleConnector(
        dataConnect: FirebaseDataConnect.instanceFor(
            connectorConfig: connectorConfig,
            sdkType: CallerSDKType.generated));
  }

  FirebaseDataConnect dataConnect;
}
