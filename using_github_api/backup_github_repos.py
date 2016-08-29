# This script will mirror all the repositories of a sepcific ornganization on your local. All the git repos will be created at the same location than 
# the script. The parameters to be passed at the run are: the name of the organization and optionally the base URL (without the repo name) to the new
# remote location
#
#
# Author: Julien Brun
# Last updated: 2016/08/26
# Contact: SciComp@nceas.ucsb.edu



import sys,os,requests

## Constants

# GItHub API URL for organization
git_org_url = "https://api.github.com/orgs/%s/repos?per_page=300"

my_destination_URL =  None

## Functions

def setting_new_remote(the_repo,remote_base_url):
	'''Add a push remote to the mirrored repo'''
	# Get the current/top path
	top_path = os.getcwd()
	# Build the repo path
	repo_path = os.path.join(top_path,the_repo + ".git")
	# Go in the repo
        os.chdir(repo_path)
	# Add the remote
	remote_url = remote_base_url + the_repo
	os.system("git remote set-url --push origin %s" %remote_url) 
	# Go back to the top level
	os.chdir(top_path)

	

def mirror_cloning_org(org):
	'''Mirror all the repositories of an organization on GitHub.com'''
	# Adapted from https://gist.github.com/caniszczyk/3856584 and https://github.com/ameygat/githuballrepo/commit/f0a81ace7f22194f1f36369568c577daa6ae8048

	# Create the URL for the organization
	my_git_org_url = git_org_url %(org)
	
	# Get the repos listing
	r = requests.get(my_git_org_url)
	
	# Handle potential request error
	if r.status_code == 200:
		rdata = r.json()
		print "{0} repositories listed under the {1} organization".format(len(rdata),org)
		for repo in rdata:
    			os.system("git clone --mirror " + repo['clone_url'])
			if my_destination_URL:
				setting_new_remote(repo['name'],my_destination_URL)
	else:
		print("request to the API failed\n Check your parameters or the API status (https://status.github.com/api/status.json)")


## Main

if __name__=='__main__':
	# Get the organization name passed as a variable as well as the new repo if defined
	if  len(sys.argv) > 2:
		my_destination_URL =  sys.argv[2]
		my_org = sys.argv[1]
	elif len(sys.argv) > 1:
		my_org = sys.argv[1]
	else:
		print("No organization was specified")
		sys.exit()

	# Mirror all the repos within the organization
	mirror_cloning_org(my_org)



