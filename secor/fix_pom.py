#!/usr/bin/env python3
import re

with open('pom.xml', 'r') as f:
    lines = f.readlines()

# Fix hadoop-mapreduce-client-core (line 180-182)
# Find the closing </dependency> tag after line 180 and insert exclusions before it
for i in range(180, 190):
    if '</dependency>' in lines[i] and 'hadoop-mapreduce-client-core' in ''.join(lines[max(0,i-5):i]):
        exclusion = '''            <exclusions>
                <exclusion>
                    <groupId>com.hadoop.gplcompression</groupId>
                    <artifactId>hadoop-lzo</artifactId>
                </exclusion>
            </exclusions>
'''
        lines[i] = exclusion + lines[i]
        break

# Fix hadoop-aws (line 185) - add to existing exclusions
for i in range(185, 205):
    if '</exclusions>' in lines[i] and 'hadoop-aws' in ''.join(lines[max(0,i-20):i]):
        new_exclusion = '''                <exclusion>
                    <groupId>com.hadoop.gplcompression</groupId>
                    <artifactId>hadoop-lzo</artifactId>
                </exclusion>
'''
        lines[i] = new_exclusion + lines[i]
        break

# Fix hadoop-openstack (line 212-214)
for i in range(212, 220):
    if '</dependency>' in lines[i] and 'hadoop-openstack' in ''.join(lines[max(0,i-5):i]):
        exclusion = '''            <exclusions>
                <exclusion>
                    <groupId>com.hadoop.gplcompression</groupId>
                    <artifactId>hadoop-lzo</artifactId>
                </exclusion>
            </exclusions>
'''
        lines[i] = exclusion + lines[i]
        break

# Write back
with open('pom.xml', 'w') as f:
    f.writelines(lines)

print("Fixed pom.xml!")
