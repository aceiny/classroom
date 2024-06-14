/*
  Warnings:

  - You are about to drop the column `verified` on the `User` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "User" DROP COLUMN "verified",
ADD COLUMN     "username" VARCHAR(255),
ALTER COLUMN "photoURL" SET DEFAULT '';
