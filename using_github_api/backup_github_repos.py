# Adapted from https://gist.github.com/caniszczyk/3856584 and https://github.com/ameygat/githuballrepo/commit/f0a81ace7f22194f1f36369568c577daa6ae8048
# Author: Julien Brun
# Last updated: 2016/08/26
# Contact: SciComp@nceas.ucsb.edu



import sys,os,requests

## Constants

# URL of the organization
git_org_url = "https://api.github.com/orgs/%s/repos?per_page=200"



## Functions

def mirror_cloning_org(org):
	'''This function allow to mirror all the repositories 
	of an organization on GitHub.com'''
	
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
	else:
		print("request to the API failed\n Check your parameters or the API status (https://status.github.com/api/status.json)")


## Main
if __name__=='__main__':
	#Get the organization passed as a variable
	if len(sys.argv) > 1:
		my_org = sys.argv[1]
	else:
		print("No organization was specified")
		sys.exit()

	# Mirror cloning all the 
	mirror_cloning_org(my_org)



