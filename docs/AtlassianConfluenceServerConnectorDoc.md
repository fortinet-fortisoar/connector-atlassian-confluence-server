## About the connector
Atlassian Confluence is a team workspace where knowledge and collaboration meet. Create, collaborate, and organize all your work in one place.
<p>This document provides information about the Atlassian Confluence Server Connector, which facilitates automated interactions, with a Atlassian Confluence Server server using FortiSOAR&trade; playbooks. Add the Atlassian Confluence Server Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Atlassian Confluence Server.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-atlassian-confluence-server</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Atlassian Confluence Server server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Atlassian Confluence Server server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Atlassian Confluence Server</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>URL of the Atlassian Confluence Server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Username</td><td>Username to access the Atlassian Confluence Server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Password</td><td>Password to access the Atlassian Confluence Server to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Spaces List</td><td>Retrieves a list of all spaces from Atlassian Confluence Server based on the input parameters you have specified.</td><td>get_spaces_list <br/>Investigation</td></tr>
<tr><td>Create Space</td><td>Creates a new Space in Atlassian Confluence Server.</td><td>create_space <br/>Investigation</td></tr>
<tr><td>Get Content List</td><td>Retrieves a list of content from Atlassian Confluence Server based on the space key, page title and other input parameters you have specified.</td><td>get_content_list <br/>Investigation</td></tr>
<tr><td>Create Content</td><td>Creates a new piece of content in Atlassian Confluence Server.</td><td>create_content <br/>Investigation</td></tr>
<tr><td>Update Content</td><td>Updates the content in Atlassian Confluence Server.</td><td>update_content <br/>Investigation</td></tr>
<tr><td>Delete Content</td><td>Deletes the content from Atlassian Confluence Server.</td><td>delete_content <br/>Investigation</td></tr>
<tr><td>Get Content List Using CQL</td><td>Retrieves a list of content from Atlassian Confluence Server based on the Confluence Query Language (CQL). For reference: https://developer.atlassian.com/server/confluence/advanced-searching-using-cql</td><td>get_content_list_using_cql <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Spaces List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Type</td><td>Select the type to filter the list of spaces returned. You can choose from following options: global or personal.
</td></tr><tr><td>Status</td><td>Select the status to filter the list of spaces returned. You can choose from following options: current or archived.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of items that this operation should return. Default: "25".
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Create Space
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Key</td><td>Specify the key of the new space that you want to create in Atlassian Confluence Server.
</td></tr><tr><td>Name</td><td>Specify the name of the new space that you want to create in Atlassian Confluence Server.
</td></tr><tr><td>Description</td><td>Specify the description of the new space that you want to create in Atlassian Confluence Server.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "key": "",
    "name": "",
    "description": {
        "plain": {
            "value": "",
            "representation": ""
        }
    },
    "metadata": {},
    "_links": {
        "collection": "",
        "base": "",
        "context": "",
        "self": ""
    }
}</pre>
### operation: Get Content List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Space Key</td><td>Specify the space key from which you want to retrieve the content.
</td></tr><tr><td>Page Title</td><td>Specify the page title to retrieve from Atlassian Confluence Server.
</td></tr><tr><td>Properties to Expand</td><td>Specify a comma separated list of properties to expand on the content. e.g. history,space,version.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of items that this operation should return. Default: "25".
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "type": "",
    "status": "",
    "title": "",
    "space": {
        "id": "",
        "key": "",
        "name": "",
        "description": {
            "plain": {
                "value": "",
                "representation": ""
            }
        },
        "metadata": {},
        "_links": {
            "self": ""
        }
    },
    "version": {
        "by": {
            "type": "",
            "username": "",
            "userKey": "",
            "displayName": "",
            "_expandable": {
                "status": ""
            }
        },
        "when": "",
        "message": "",
        "number": "",
        "minorEdit": "",
        "hidden": ""
    },
    "ancestors": [
        {
            "id": "",
            "type": "",
            "status": "",
            "ancestors": [],
            "operations": [],
            "children": {},
            "descendants": {},
            "body": {},
            "metadata": {},
            "restrictions": {},
            "_links": {
                "self": ""
            }
        }
    ],
    "operations": [],
    "children": {},
    "descendants": {},
    "container": {
        "id": "",
        "key": "",
        "name": "",
        "description": {
            "plain": {
                "value": "",
                "representation": ""
            }
        },
        "metadata": {},
        "_links": {
            "self": ""
        }
    },
    "body": {
        "view": {
            "value": "",
            "representation": "",
            "_expandable": {
                "content": ""
            }
        }
    },
    "metadata": {},
    "restrictions": {},
    "_links": {
        "collection": "",
        "base": "",
        "context": "",
        "self": ""
    }
}</pre>
### operation: Create Content
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Content Type</td><td>Specify the content type that you want to create in Atlassian Confluence Server. e.g. page or blogpost.
</td></tr><tr><td>Space Key</td><td>Specify the space key on which to create the content.
</td></tr><tr><td>Title</td><td>Specify the title of the new content that you want to create in Atlassian Confluence Server.
</td></tr><tr><td>Body</td><td>Specify the body of the new content that you want to create in Atlassian Confluence Server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Update Content
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Content ID</td><td>Specify the content ID that you want to update in Atlassian Confluence Server.
</td></tr><tr><td>Version Number</td><td>Specify the new version number for the content that you want to update in Atlassian Confluence Server. Note: To update a piece of content you must increment the version number, supplying the number of the version you are creating.
</td></tr><tr><td>Content Type</td><td>Specify the type of the content that you want to update in Atlassian Confluence Server. e.g. page or blogpost.
</td></tr><tr><td>Space Key</td><td>Specify the space key on which to update the content.
</td></tr><tr><td>Title</td><td>Specify the title of the content that you want to update in Atlassian Confluence Server.
</td></tr><tr><td>Body</td><td>Specify the body of the content that you want to update in Atlassian Confluence Server.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "type": "",
    "status": "",
    "title": "",
    "space": {
        "id": "",
        "key": "",
        "name": "",
        "description": {
            "plain": {
                "value": "",
                "representation": ""
            }
        },
        "metadata": {},
        "_links": {
            "self": ""
        }
    },
    "version": {
        "by": {
            "type": "",
            "username": "",
            "userKey": "",
            "displayName": "",
            "_expandable": {
                "status": ""
            }
        },
        "when": "",
        "message": "",
        "number": "",
        "minorEdit": "",
        "hidden": ""
    },
    "ancestors": [
        {
            "id": "",
            "type": "",
            "status": "",
            "ancestors": [],
            "operations": [],
            "children": {},
            "descendants": {},
            "body": {},
            "metadata": {},
            "restrictions": {},
            "_links": {
                "self": ""
            }
        }
    ],
    "operations": [],
    "children": {},
    "descendants": {},
    "container": {
        "id": "",
        "key": "",
        "name": "",
        "description": {
            "plain": {
                "value": "",
                "representation": ""
            }
        },
        "metadata": {},
        "_links": {
            "self": ""
        }
    },
    "body": {
        "view": {
            "value": "",
            "representation": "",
            "_expandable": {
                "content": ""
            }
        }
    },
    "metadata": {},
    "restrictions": {},
    "_links": {
        "collection": "",
        "base": "",
        "context": "",
        "self": ""
    }
}</pre>
### operation: Delete Content
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Content ID</td><td>Specify the content ID that you want to delete from Atlassian Confluence Server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Content List Using CQL
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>CQL</td><td>Specify the Confluence Query Language (CQL) based on which to retrieve the content.
</td></tr><tr><td>CQL Context</td><td>Specify the context to execute a cql search in, this is the json serialized form of SearchContext.
</td></tr><tr><td>Properties to Expand</td><td>Specify a comma separated list of properties to expand on the content. e.g. history,space,version.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of items that this operation should return. Default: "25".
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - atlassian-confluence-server - 1.0.0` playbook collection comes bundled with the Atlassian Confluence Server connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Atlassian Confluence Server connector.

- Create Content
- Create Space
- Delete Content
- Get Content List
- Get Content List Using CQL
- Get Spaces List
- Update Content

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
