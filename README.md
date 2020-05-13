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

In the login screen, tap on the gear icon at the top right corner of the screen to enter the base URL of the Traxiem server and the database.

In the iOS Settings for Traxiem, allow banners, sounds, and badges notifications, and enable Background Refresh. The logged in user will receive notifications when a new defect has been assigned to the user or when any modifications are made to a defect that the user currently owns.

## Development

### Login Scene

#### Overview

The Login Scene displays a username textbox, a password textbox, a repo button, and a settings icon. When the user selects the repo button, display the list of repos to choose. When the user selects the settings icon, display textboxes for the base URL of the Traxiem server and the database. Once the username, password, repo, database, and the base URL of the Traxiem server are provided by the user, login the user by invoking a Traxiem REST API. 

#### Diagram

<pre>
<a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getrepos-api'>getRepos API</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#login-api'>login API</a>
</pre>

#### API Details

##### login API

1. Call the function `login(_ usernameText: String, _ passwordText: String)` using the username and password that the user provided. 

2. Make the function `login(_ usernameText: String, _ passwordText: String)` call the `login(with username: String, password: String, repo: String, db: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager` using the username, password, repo, and database that the user provided. This will get the HTTP Method (POST) and the URL request required to execute the API call.

3. Invoke the Traxiem login REST API call.

	* If the Traxiem login REST API call is successfully made, decode the data to the struct `AuthToken`.
	
		1. Store the token in the class `KeychainHelper` to make the token accessible for other Traxiem REST API calls. 

	* If the Traxiem login REST API call fails, present an alert with the error message.

### Repo Selection Scene

#### Overview

The Repo Selection Scene displays a list of repos. The list of repos is obtained from the result of invoking a Traxiem REST API. The user can choose any repo from the list.

#### API Details

##### getRepos API

1. When the view controller `RepoSelectionVC` is loaded, call the function `fetchRepos()`.

2. Make the function `fetchRepos()` call the `getRepos(completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the HTTP Method (GET) and the URL request required to execute the API call.

3. Invoke the Traxiem getRepos REST API call.

	* If the Traxiem getRepos REST API call is successfully made, decode the data to an array of Repo structs `[Repo]`. 

		1. In the function `tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell`, configure each cell in the table using the repos inside the array of Repo structs `[Repo]`.

	* If the Traxiem getRepos REST API call fails, print the error status to the console.

### Record List Scene

#### Overview

The Record List Scene displays a list of records, either a list of records assigned to the logged in user or a list of records reported by the logged in user. The list of records is obtained by the results of invoking Traxiem query REST APIs. 

First, determine whether the query already exists under the Personal Folder in Traxiem for the logged in user. If the query doesn't already  exist, create the query, create the result set of the query, and get the result set of the query. 

If the query already exists, it is not necessary to create the query again. Instead, create the result set of the existing query and then get the result set of the query.

Give the user the option to logout.

#### Diagram

<pre>
<a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getfolders-api'>getFolders API</a>
  |
  Query not exists -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#createquery-api'>createQuery API</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#createresultset-api'>createResultSet API</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getresultset-api'>getResultSet API</a>
  |
  Query exists -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#createresultset-api'>createResultSet API</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getresultset-api'>getResultSet API</a>
</pre>

#### API Details

##### getFolders API
1. Whenever the view controller `RecordListVC` is loaded or refreshed, call the function `getFolders()`. 

2. Make the function `getFolders()` call the `getFolders(completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (GET), and the URL request required to execute the API call.

3. Invoke the Traxiem getFolders REST API call.

	* If the Traxiem getFolders REST API call is successfully made, decode the data to an array of Folder structs `[Folder]`. 

		* If the query doesn't already exist under the Personal Folder in Traxiem for the logged in user, see the `Query not exists` branch in the [Diagram](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#diagram).
		
		* If the query already exists under the Personal Folder in Traxiem for the logged in user, see the `Query exists` branch in the [Diagram](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#diagram). 	
	* If the Traxiem getFolders REST API call fails, print the error status to the console.

##### createQuery API

1. Call the function `createQuery(in parentFolderDbId: String, with name: String)` using the dbId of the personal folder and the name of the query. 

2. Make the function `createQuery(in parentFolderDbId: String, with name: String)` call the `createQuery(in parentFolderDbId: String, named name: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, URL request, the HTTP Method (POST), and the request body required to execute the API call. For the request body, use the name of the query to obtain the the query definition from the .json file. The .json file has the same name as the query.
				
3. Invoke the Traxiem createQuery REST API call.

	* If the Traxiem createQuery REST API call is successfully made, decode the data to the struct `QueryDef`.
	
		1. See [createResultSet API](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#createresultset-api) to create the result set of the query.
		
	* If the Traxiem createQuery REST API call fails, print the error status to the console.

##### createResultSet API	
	
1. Call the `createResultSet(for queryDbId: String)` function using the dbId of the query. 
				
2. Make the function `createResultSet(for queryDbId: String)` call the `createResultSet(for queryDbId: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, URL request, the HTTP Method (POST), and the request body required to execute the API call. The request body contains `["pageSize": "999"]`. 
			
3. Invoke the Traxiem createResultSet REST API call.
		
	* If the Traxiem createResultSet REST API call is successfully made, the decode the data to the struct `ResultSet`.

		1. See [getResultSet API](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getresultset-api) to get the result set of the query.
		
	* If the Traxiem createResultSet REST API call fails, print the error status to the console.

##### getResultSet API

1. Call the `getResultSet(of resultSetId: String, for queryDbId: String)` function using the Id of the result set and the dbId of the query.
		
2. Make the function `getResultSet(of resultSetId: String, for queryDbId: String)` call the `getResultSet(of resultSetId: String, for queryDbId: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (GET), and the URL request required to execute the API call.
					 
3. Invoke the Traxiem getResultSet REST API call.
			
	* If the Traxiem getResultSet REST API call is successfully made, decode the data to the struct `ResultSetPage`. 
								
		1. In the function `tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell`, configure each cell in the table as a `RecordListCell` using the defects inside the array of ResultSetRow structs `[ResultSetRow]`.
				
	* If the Traxiem getResultSet REST API call fails, print the error status to the console.

##### logout API

1. Call the function `logout()`.

2. Make the function `logout()` call the `logoff(completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, the HTTP Method (POST), and the URL request required to execute the API call.

3. Invoke the Traxiem logout REST API call.

	* If the Traxiem logout REST API call is successfully made, dismiss the view controller to return to the [Login Scene](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#login-scene). 

	* If the Traxiem logout REST API call fails, print the error status to the console.
	
### Record Detail Scene

#### Overview

The Record Detail Scene displays a list of fields of a record. The list of record fields is obtained by the results of invoking Traxiem record REST APIs. There are three possible actions a user can take: modify, change state, or delete the record. 

If the modify action is selected, make the record enter interactive editing mode and allow the user to modify the editable fields of the record. When the user edits a field, except for the `Headline` and `Description` fields, display a list of possible field values to choose. Once the editing is completed, save the updated fields of the record. 

If the change state action is selected, display a list of possible states the record can change to. Once the user selects a state, the process is the same as when the modify action is selected.

If the delete action is selected, delete the record.

#### Diagram

<pre>
<a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getrecord-api'>getRecord API</a>
  |
  Modify -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#modifyrecord-api'>modifyRecord API (edit)</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getfield-api'>getField API</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#modifyrecord-api'>modifyRecord API (save)</a>
  |
  Change state -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getrecordtype-api'>getRecordType API</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#modifyrecord-api'>modifyRecord API (edit)</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getfield-api'>getField API</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#modifyrecord-api'>modifyRecord API (save)</a>
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

1.  Call the function `modifyRecord(_ recordId: String, _ operation: String, body: [String: [[String: String?]]], actionName: String?)` using the record Id, the operation, the request body, and the action name (Modify). The modifyRecord API can be used to fulfill two operations:

	* Edit: Set the opertion parameter to `Edit` and the request body as `[:]`. 
	
	* Save: Set the opertion parameter to `Commit` and the request body will be filled once the user presses the `Done` button.
	
2. Make the function `modifyRecord(_ recordId: String, _ operation: String, body: [String: [[String: String?]]], actionName: String?)` call the `modifyRecord(with recordId: String, body: [String: [[String: String?]]], operation: String, actionName: String?, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (PATCH), and the URL request required to execute the API call. 
	
3. Invoke the Traxiem modifyRecord REST API call.

	* If the Traxiem modifyRecord REST API call is successfully made, decode the data to the struct `Record`. 
	
		* If the `Commit` operation was used to invoke the Traxiem modifyRecord REST API call, see [getRecord API](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getrecord-api) to display the updated fields in the record.
		
	* If the Traxiem modifyRecord REST API call fails, print the error status to the console.

##### deleteRecord API

1. Call the function `deleteRecord(_ recordId: String)` using the record Id of the record.

2. Make the function `deleteRecord(_ recordId: String)` call the `deleteRecord(with recordId: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (DELETE), and the URL request required to execute the API call.

3. Invoke the Traxiem deleteRecord REST API call.

	* If the Traxiem deleteRecord REST API call is successfully made, reload the data in the [Record List Scene](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#record-list-scene).
	
	* If the Traxiem deleteRecord REST API call fails, print the error status to the console.

### State Selection Scene

#### Overview

The State Selection Scene displays a list of possible states that the record can change to. The list of states is obtained from the result of invoking a Traxiem record REST API. The user can choose any state from the list.

#### API Details

##### getRecordType API

1. When the view controller `StateSelectionVC` is loaded, call the function `getRecordType()`.

2. Make the function `getRecordType()` call the `getRecordType(completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (GET), and the URL request required to execute the API call.

3. Invoke the Traxiem getRecordType REST API call.

	* If the Traxiem getRecordType REST API call is successfully made, decode the data to the struct `RecordType`. 
	
		1. In the function `tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell`, configure each cell in the table using the possible states inside the array of State structs `[State]`.
	
	* If the Traxiem getRecordType REST API call fails, print the error status to the console.

### Field Selection Scene

#### Overview

The Field Selection Scene displays a list of field values for a specific field of a record. The list of field values is obtained from the result of invoking a Traxiem REST API. The user can choose any field value from the list.

#### API Details

##### getField API

1. When the view controller `FieldSelectionVC` is loaded, call the function `getField(_ recordId: String, _ fieldName: String)` using the record Id of the record and the name of the selected field.

2. Make the function `getField(_ recordId: String, _ fieldName: String)` call the `getField(of recordId: String, with fieldName: String, completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (GET), and the URL request required to execute the API call.

3. Invoke the Traxiem getField REST API call.

	* If the Traxiem getRecordType REST API call is successfully made, decode the data to the struct `Field`. 

		1. In the function `tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell`, configure each cell in the table using the field values inside the `fieldChoiceList` array.

	* If the Traxiem getField REST API call fails, print the error status to the console.

### Create Record Scene

#### Overview

The Create Record Scene displays a list of empty fields of a newly created record. The list of record fields is obtained by the results of invoking a Traxiem REST API. When the record is created, make the record enter interactive editing mode and allow the user to modify the editable fields of the record. When the user edits a field, except for the `Headline` and `Description` fields, display a list of possible field values to choose. Once the editing is completed, save the updated fields of the record. 

#### Diagram

<pre>
<a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#createrecord-api'>createRecord API</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#getfield-api'>getField API</a> -> <a href='https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#modifyrecord-api'>modifyRecord API (save)</a>
</pre>

#### API Details

##### createRecord API

1. When the view controller `CreateRecordVC` is loaded, call the function `createRecord()`.

2. Make the function `createRecord()` call the `createRecord(completion: @escaping(Result<Data?, ApiError>) -> Void)` function in the class `TRXNetworkManager`. This will get the token, repo, the HTTP Method (POST), the `Edit` operation, the empty request body, and the URL request required to execute the API call.

3. Invoke the Traxiem createRecord REST API call.

	* If the Traxiem createRecord REST API call is successfully made, decode the data to the struct `Record`. 

		1. In the function `tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell`, configure each cell in the table as a `RecordFieldCell` using the fields inside the array of Field structs `[Field]`.

	* If the Traxiem createRecord REST API call fails, print the error status to the console.

### Notifications

Every five minutes, including when the app is in the background, check whether there are any new defects assigned to the logged in user or if any modifications have been made to a defect that the user currently owns. This is done using the same Traxiem query REST APIs that are implemented for the [Record List Scene](https://github01.hclpnp.com/traxiem/traxiem/tree/master/samples/traxiem-ios#record-list-scene). If there is at least one record in the result set of the query, trigger a notification for each record.
