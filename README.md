# hello-world

Hello world!

I'm Rosalba Monterrosas and I am a computer science major. I have experience in C, C++, and Python. I'm excited to learn more and improve my coding skills!

This is a place where I store ideas, resources, and share and discuss things with others.






# Traxiem Defect Tracking App for iOS
Traxiem iOS app for defect tracking that allows the creation, editing, and deletion of defects.

## Usage
This app allows the user to login using the username, password, and selected repo. The app then displays the list of defects assigned to the user. A tab bar at the bottom of the screen allows the user to switch to the list of defects reported by the user. The user can swipe left on a specific defect to delete it, and tap the plus icon to create a new defect. The user can tap on a specific defect to view more details about the defect. When viewing a defect, the user has the option to modify, change state, or delete the defect. Notifications are sent to the user when a new defect has been assigned to the user and when any modifications are made to a defect that the user currently owns.

## Getting Started
These instructions will get you a copy of the Xcode project on your local machine for development and testing purposes.
### Prerequisites
Xcode needs to be downloaded from the App Store.
Traxiem needs to be installed.

## Build the App
To build the app in Xcode, click on Product in the menu bar and then click on Clean Build Folder.
To run the app in Xcode, click on Product in the menu bar and then click on Run.
To build and then run the app, click on the play icon in the top left corner.

## Install and Update
To run the app in an iOS Simulator in Xcode, pick an iOS 12.0 or later Simulator from the list provided or choose the Download Simulators option. Then, build and run the app.

To run the app on an iPhone, connect the iPhone to your local machine. In Xcode, select the Additional Simulators option and then click on the Devices tab. The iPhone will appear in the devices list in the left column. Select the iPhone and then build and run the app.

## License
/*******************************************************************************

(c) Copyright HCL Technologies Ltd. 2020. MIT Licensed!

*******************************************************************************/

## Configuration Properties
### Xcode
Select the target and go to the Signing & Capabilities tab. Add the Background Modes capability and select Background fetch and Background processing.
debug flag
### App
In the login screen, tap on the gear icon at the top right corner of the screen to enter the URL of the Traxiem server.
Enable notifications for the app in iOS Settings in order to receive banners, sound, and badge notifications. The user will receive notifications when a new defect has been assigned to the user and when any modifications are made to a defect that the user currently owns.

## Development
For each scene: View controller, Models, Data Source, specific API for viewing and for actions, Cells
Queries
### App/Scene Delegate

### Login Scene
Login authorization tokens
Logout API
#### Settings Scene
#### Repo Selection Scene
#### Network Manager

### Record List Scene

#### Overview

The Record List Scene displays a list of records, either a list of records assigned to the logged in user or a list of records reported by the logged in user. The list of records is obtained by the results of invoking Traxiem query REST APIs. First, determine whether the query already exists under the Personal Folder in Traxiem for the logged in user. If the query doesn't already  exist, create the query, create the result set of the query, and get the result set of the query. If the query already exists, it is not necessary to create the query again. Instead, create the result set of the existing query and then get the result set of the query.

#### Diagram

<pre>
<a href='https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#getfolders-api'>getFolders API</a>
  |
  Query not exists -> <a href='https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#createquery-api'>createQuery API</a> -> <a href='https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#createresultset-api'>createResultSet API</a> -> <a href='https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#getresultset-api'>getResultSet API</a>
  |
  Query exists -> <a href='https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#createresultset-api'>createResultSet API</a> -> <a href='https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#getresultset-api'>getResultSet API</a>
</pre>

#### API Details

##### getFolders API
1. Whenever the view controller `RecordListVC` is loaded or refreshed, call the function `getFolders()`. 

2. Make the function `getFolders()` call the `getFolders(completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (GET), and the URL request required to execute the API call.

3. Invoke the Traxiem getFolders REST API call.

	* If the Traxiem getFolders REST API call is successfully made, decode the data to an array of Folder structs `[Folder]`. 

		* If the query doesn't already exist under the Personal Folder in Traxiem for the logged in user, see the `Query not exists` branch in the [Diagram](https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#diagram).
		
		* If the query already exists under the Personal Folder in Traxiem for the logged in user, see the `Query exists` branch in the [Diagram](https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#diagram). 	
	* If the Traxiem getFolders REST API call fails, print the error status to the console.

##### createQuery API

1. Call the function `createQuery(in parentFolderDbId: String, with name: String)` using the dbId of the personal folder and the name of the query. 

2. Make the function `createQuery(in parentFolderDbId: String, with name: String)` call the `createQuery(in parentFolderDbId: String, named name: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, URL request, the HTTP Method (POST), and the request body required to execute the API call. For the request body, use the name of the query to obtain the the query definition from the .json file. The .json file has the same name as the query.
				
3. Invoke the Traxiem createQuery REST API call.

	* If the Traxiem createQuery REST API call is successfully made, decode the data to the struct `QueryDef`.
	
		1. See [createResultSet API](https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#createresultset-api) to create the result set of the query.
		
	* If the Traxiem createQuery REST API call fails, print the error status to the console.

##### createResultSet API	
	
1. Call the `createResultSet(for queryDbId: String)` function using the dbId of the query. 
				
2. Make the function `createResultSet(for queryDbId: String)` call the `createResultSet(for queryDbId: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, URL request, the HTTP Method (POST), and the request body required to execute the API call. The request body contains `["pageSize": "999"]`. 
			
3. Invoke the Traxiem createResultSet REST API call.
		
	* If the Traxiem createResultSet REST API call is successfully made, the decode the data to the struct `ResultSet`.

		1. See [getResultSet API](https://github.com/rosalbamonterrosas/hello-world/blob/master/README.md#getresultset-api) to get the result set of the query.
		
	* If the Traxiem createResultSet REST API call fails, print the error status to the console.

##### getResultSet API

1. Call the `getResultSet(of resultSetId: String, for queryDbId: String)` function using the Id of the result set and the dbId of the query.
		
2. Make the function `getResultSet(of resultSetId: String, for queryDbId: String)` call the `getResultSet(of resultSetId: String, for queryDbId: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (GET), and the URL request required to execute the API call.
					 
3. Invoke the Traxiem getResultSet REST API call.
			
	* If the Traxiem getResultSet REST API call is successfully made, decode the data to the struct `ResultSetPage`. 
								
		1. In the function `tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell`, configure each cell in the table as a `RecordListCell` using the defects inside the array of ResultSetRow structs `[ResultSetRow]`.
				
	* If the Traxiem getResultSet REST API call fails, print the error status to the console.
	
### Record Detail Scene

#### Overview

The Record Detail Scene displays a list of fields of a record. The list of records is obtained by the results of invoking Traxiem record REST APIs. There are three possible actions a user can take: modify, change state, or delete the record. If the modify action is selected, make the record enter interactive editing mode and allow the user to be able to modify the editable fields of the record. If the change state action is selected, allow the user to choose the desired state and then make the record enter interactive editing mode once the user taps on the done button. Save the updated fields of the record when the user taps on the done button. If the delete action is selected, delete the record.

#### Diagram

<pre>
<a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getrecord-api'>getRecord API</a>
  |
  Modify -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#modifyrecord-api'>modifyRecord API</a> -> Done button -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#modifyrecord-api'>modifyRecord API</a>
  |
  Change state -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getrecordtype-api'>getRecordType API</a> -> State done button -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#modifyrecord-api'> modifyRecord API</a> -> Done button -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#modifyrecord-api'>modifyRecord API</a>
  |
  Delete -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#deleterecord-api'>deleteRecord API</a> 
</pre>

#### API Details

##### getRecord API

1. When the view controller `RecordDetailVC` is loaded, call the function `getRecord(_ recordId: String)` using the record Id of the selected record from the table.

2. Make the function `getRecord(_ recordId: String)` call the `getRecord(with recordId: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (GET), and the URL request required to execute the API call.

3. Invoke the Traxiem getRecord REST API call.

	* If the Traxiem getRecord REST API call is successfully made, decode the data to the struct `Record`. 

		1. In the function `tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell`, configure each cell in the table as a `RecordFieldCell` using the fields inside the array of Field structs `[Field]`.
	
	* If the Traxiem getRecord REST API call fails, print the error status to the console.
	
##### modifyRecord API

1.  Call the function `modifyRecord(_ recordId: String, _ operation: String, body: [String: [[String: String?]]], actionName: String?)` using the record Id, the operation, the request body, and the action name (Modify).  
	
2. Make the function `modifyRecord(_ recordId: String, _ operation: String, body: [String: [[String: String?]]], actionName: String?)` call the `modifyRecord(with recordId: String, body: [String: [[String: String?]]], operation: String, actionName: String?, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (PATCH), and the URL request required to execute the API call. 
	
3. Invoke the Traxiem modifyRecord REST API call.

	* If the Traxiem modifyRecord REST API call is successfully made, decode the data to the struct `Record`. 
	
		* If the `Commit` operation was used to invoke the Traxiem modifyRecord REST API call, see [getRecord API](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getrecord-api) to view the updated fields in the record.
		
	* If the Traxiem modifyRecord REST API call fails, print the error status to the console.

##### getRecordType API

1. When the view controller `StateSelectionVC` is loaded, call the function `getRecordType()`.

2. Make the function `getRecordType()` call the `getRecordType(completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (GET), and the URL request required to execute the API call.

3. Invoke the Traxiem getRecordType REST API call.

	* If the Traxiem getRecordType REST API call is successfully made, decode the data to the struct `RecordType`. 
	
		1. In the function `tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell`, configure each cell in the table using the possible states inside the array of State structs `[State]`.
	
	* If the Traxiem getRecordType REST API call fails, print the error status to the console.

##### deleteRecord API

1. Call the function `deleteRecord(_ recordId: String)` using the record Id of the selected record.

2. Make the function `deleteRecord(_ recordId: String)` call the `deleteRecord(with recordId: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (DELETE), and the URL request required to execute the API call.

3. Invoke the Traxiem deleteRecord REST API call.

	* If the Traxiem deleteRecord REST API call is successfully made, reload the data in the [Record List Scene](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#record-list-scene).
	
	* If the Traxiem deleteRecord REST API call fails, print the error status to the console.

#### Field Selection Scene	
#### Description Scene

### Create Record Scene
#### Field Selection Scene
#### Description Scene

### Notifications
