# -*- coding: utf-8 -*-
# the cpu dump not working on win10 but on xp is good

import my_debugger
debugger = my_debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to:")
debugger.attach(int(pid))

threadList = debugger.enumerate_threads()
print threadList
for thread in threadList:
	thread_context = debugger.get_thread_context(thread)
	print "[*] Dumping registers for thread ID:0x%08x" % thread
	print "[**] EIP:0x%08x" % thread_context.Eip
	print "[**] ESP:0x%08x" % thread_context.Esp
	print "[**] EBP:0x%08x" % thread_context.Ebp
	print "[**] EAX:0x%08x" % thread_context.Eax
	print "[**] EBX:0x%08x" % thread_context.Ebx
	print "[**] ECX:0x%08x" % thread_context.Ecx
	print "[**] EDX:0x%08x" % thread_context.Edx
	print "[*] END DUMP"

debugger.detach()