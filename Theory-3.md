# Theory-3: Projects
*	**Differences between flight and ground:**
	*	**Product Complexity (CPLX):** flight has cplx in the range [nom,xhigh], while ground has cplx in the range [vlow,high]. This means the tasks in project flights are very difficult and may contain highly coupled objects, analysis of noisy data, complex parallelization, distributed computing, unstructured data etc., whereas the tasks in flight go only as far as evaluating moderate-level expressions, simple triggers, voice recognition, I/O optimization etc.
	*	**Required Software Reliability (RELY):** flight has rely in the range[nom,vhigh], while ground has rely in the range[vlow,high]. This means the effect of software failure is slightly to moderately inconvenience in JPL Ground systems, might also lead to financial loss, but it cannot lead to loss of human life, which is quite possible in JPL Flight systems.
	*	**Lines of Code (KLOC):** Quite evidently, JPL Flight systems has larger codebase due to increased complexity of the product and risk of software reliability.

*	**Differences between osp and osp2:**
	*	**Multisite Development (SITE):** osp has nominal (3) value for site, whereas, osp2 has extra high value for site. Maybe the management decided to discuss the proceedings of the 	project over tele-conferences or other multimedia means rather than discussing them over emails.
	*	**Precedentedness (PREC):** osp has very low to low value for prec, whereas osp2 has prec in the range[nom,vhigh]. This actually makes sense because as a project develops, understanding of product objectives increases, which may enable management to identify related software systems, and do away with developing new and complex systems.
	*	**Use of Software Tools (TOOL):** osp has low to nominal value for tool, whereas, osp2 has only very high value for tool. The management decided to move from basic lifecycle tools to strong, mature, proactive lifecycle tools, well integrated with processes and methods.

